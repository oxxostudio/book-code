# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import QImage, QPixmap
import sys, cv2, threading, random

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(480, 320)
        self.setUpdatesEnabled(True)
        self.ocv = True
        self.window_w, self.window_h = 300, 220   # 設定視窗長寬
        self.scale = 0.58                         # 影片高度的比例
        self.photo= False    # 按下拍照紐時的參考變數，預設 False
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')    # 設定存檔影片格式
        self.recorderType = False                        # 設定是否處於錄影狀態，預設 False
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0,0,self.window_w,int(self.window_w*self.scale)) # 設定 QLabel 位置和尺寸
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(10,self.window_h-40,70,30)      # 設定拍照鈕的位置和尺寸
        self.btn1.setText('拍照')
        self.btn1.clicked.connect(self.takePhoto)             # 按下按鈕觸發拍照
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(80,self.window_h-40,70,30)      # 設錄影照鈕的位置和尺寸
        self.btn2.setText('錄影')
        self.btn2.clicked.connect(self.recordVideo)           # 按下按鈕觸發錄影或停止錄影

    def resizeEvent(self, event):
        self.window_w = Form.width()    # 取得視窗寬度
        self.window_h = Form.height()   # 取得視窗高度
        self.label.setGeometry(0,0,self.window_w,int(self.window_w*self.scale))  # 設定 QLabel 尺寸
        self.btn1.setGeometry(10,self.window_h-40,70,30)  # 設定按鈕位置
        self.btn2.setGeometry(80,self.window_h-40,200,30) # 設定按鈕位置

    def closeEvent(self, event):
        self.ocv = False            # 關閉視窗後，設定成 False
        try:
            self.output.release()   # 關閉視窗後，釋放儲存影片的資源
        except:
            pass                    # 如果沒有按下錄製影片按鈕，就略過

    # 存檔時使用隨機名稱的函式
    def rename(self):
        return str(random.random()*10).replace('.','')

    # 按下拍照扭的動作
    def takePhoto(self):
        self.photo = True           # 變數設定為 True

    # 按下錄影按鈕的動作
    def recordVideo(self):
        if self.recorderType == False:
            # 如果按下按鈕時沒有在錄影
            # 設定錄影的檔案
            self.output = cv2.VideoWriter(f'{self.rename()}.mp4', self.fourcc, 20.0, (self.window_w,int(self.window_w*self.scale)))
            self.recorderType = True                   # 改為 True 表示正在錄影
            self.btn2.setGeometry(80,self.window_h-40,200,30)  # 因為內容文字變多，改變尺寸
            self.btn2.setText('錄影中，點擊停止並存擋')
        else:
            # 如果按下按鈕時正在錄影
            self.output.release()                    # 釋放檔案資源
            self.recorderType = False                # 改為 False 表示停止錄影
            self.btn2.setGeometry(80,self.window_h-40,70,30)   # 改變尺寸
            self.btn2.setText('錄影')

    def opencv(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while self.ocv:
            ret, frame = cap.read()             # 讀取影格
            if not ret:
                print("Cannot receive frame")
                break
            frame = cv2.resize(frame, (self.window_w, int(self.window_w*self.scale)))  # 改變尺寸符合視窗
            if self.photo == True:
                self.photo = False                   # 按下拍照鈕時，會先設定 True，觸發後再設回 False
                name = self.rename()                 # 重新命名檔案
                cv2.imwrite(f'{name}.jpg', frame) # 儲存圖片
            if self.recorderType == True:
                self.output.write(frame)             # 按下錄影時，將檔案儲存到 output
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 改為 RGB
            height, width, channel = frame.shape
            bytesPerline = channel * width
            img = QImage(frame, width, height, bytesPerline, QImage.Format.Format_RGB888)
            # img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)  # PyQt5 寫法
            self.label.setPixmap(QPixmap.fromImage(img))   # 顯示圖片

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    video = threading.Thread(target=Form.opencv)
    video.start()
    Form.show()
    sys.exit(app.exec())

