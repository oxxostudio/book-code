# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import QImage, QPixmap
import sys, cv2, threading

app = QtWidgets.QApplication(sys.argv)
window_w, window_h = 300, 200

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(window_w, window_h)

def windowResize(self):
    global window_w, window_h
    window_w = Form.width()
    window_h = Form.height()
    label.setGeometry(0,0,window_w,window_h)

Form.resizeEvent = windowResize

ocv = True                     # 一開始設定為 True
def closeOpenCV(self):
    global ocv
    ocv = False                # 關閉視窗時設定為 False
Form.closeEvent = closeOpenCV  # 關閉視窗事件發生時，執行 closeOpenCV 函式

label = QtWidgets.QLabel(Form)
label.setGeometry(0,0,window_w,window_h)

def opencv():
    global window_w, window_h, ocv
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    # while 迴圈改為 ocv
    while ocv:
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame")
            break
        frame = cv2.resize(frame, (window_w, window_h))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytesPerline = channel * width
        img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)
        # img = QImage(frame, width, height, bytesPerline, QImage.Format_RGB888)  # PyQt5 寫法
        label.setPixmap(QPixmap.fromImage(img))

video = threading.Thread(target=opencv)
video.start()

Form.show()
sys.exit(app.exec())

