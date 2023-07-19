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
        self.window_w, self.window_h = 300, 200    # 定義預設長寬尺寸
        self.ocv = True
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0,0,self.window_w,self.window_h)  # 使用變數

    def resizeEvent(self, event):
        self.window_w = Form.width()      # 讀取視窗寬度
        self.window_h = Form.height()     # 讀取視窗高度
        self.label.setGeometry(0,0,self.window_w,self.window_h)  # 設定 QLabel 長寬

    def closeEvent(self, event):
        self.ocv = False                # 關閉視窗時設定為 False

    def opencv(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while self.ocv:
            ret, frame = cap.read()
            if not ret:
                print("Cannot receive frame")
                break
            frame = cv2.resize(frame, (self.window_w, self.window_h))  # 使用變數
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytesPerline = channel * width
            img = QImage(frame, width, height, bytesPerline, QImage.Format.Format_RGB888)
            # img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)  # PyQt5 寫法
            self.label.setPixmap(QPixmap.fromImage(img))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    video = threading.Thread(target=Form.opencv)
    video.start()
    Form.show()
    sys.exit(app.exec())

