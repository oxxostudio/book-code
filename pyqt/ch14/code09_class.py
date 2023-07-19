# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import QImage, QPixmap
import sys, cv2, threading, random

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)     # 建立 QLabel
        self.label.setGeometry(0,0,300,200)     # 設定 QLabel 大小和視窗相同

    def opencv(self):
        cap = cv2.VideoCapture(0)      # 設定攝影機鏡頭
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            ret, frame = cap.read()    # 讀取攝影機畫面
            if not ret:
                print("Cannot receive frame")
                break
            frame = cv2.resize(frame, (300, 200))   # 改變尺寸和視窗相同
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 轉換成 RGB
            height, width, channel = frame.shape    # 讀取尺寸和 channel數量
            bytesPerline = channel * width          # 設定 bytesPerline ( 轉換使用 )
            # 轉換影像為 QImage，讓 PyQt6 可以讀取
            img = QImage(frame, width, height, bytesPerline, QImage.Format.Format_RGB888)
            # img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)  # PyQt5 寫法
            self.label.setPixmap(QPixmap.fromImage(img)) # QLabel 顯示影像

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    video = threading.Thread(target=Form.opencv)
    video.start()
    Form.show()
    sys.exit(app.exec())

