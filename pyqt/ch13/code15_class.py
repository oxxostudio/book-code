# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys, cv2, threading

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(480, 320)
        self.setUpdatesEnabled(True)
        self.ui()
        self.ocv = True

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 480, 320)

    def closeEvent(self):
        self.ocv = False

    def opencv(self):
        cap = cv2.VideoCapture(0)         # 設定攝影機鏡頭
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while self.ocv:
            ret, frame = cap.read()       # 讀取攝影機畫面
            if not ret:
                print("Cannot receive frame")
                break
            frame = cv2.resize(frame, (480, 320))   # 改變尺寸和視窗相同
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # 轉換成 RGB
            height, width, channel = frame.shape    # 讀取尺寸和 channel數量
            bytesPerline = channel * width          # 設定 bytesPerline ( 轉換使用 )
            # 轉換影像為 QImage，讓 PyQt 可以讀取
            qimg = QImage(frame, width, height, bytesPerline, QImage.Format.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(qimg)) # QLabel 顯示影像


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    video = threading.Thread(target=Form.opencv)    # 建立 OpenCV 的 Thread
    video.start()                                   # 啟動 Thread
    Form.show()
    sys.exit(app.exec())

