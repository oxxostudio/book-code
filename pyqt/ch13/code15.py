# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys, cv2, threading

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)    # 建立 QLabel
label.setGeometry(0,0,300,200)          # 設定 QLabel 位置尺寸

ocv = True             # 設定全域變數，讓關閉視窗時 OpenCV 也會跟著關閉
def closeOpenCV():
    global ocv
    ocv = False        # 關閉視窗時，將 ocv 設為 False

MainWindow.closeEvent = closeOpenCV  # 設定關閉視窗的動作

# 讀取攝影機的函式
def opencv():
    global ocv
    cap = cv2.VideoCapture(0)         # 設定攝影機鏡頭
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while ocv:
        ret, frame = cap.read()       # 讀取攝影機畫面
        if not ret:
            print("Cannot receive frame")
            break
        frame = cv2.resize(frame, (480, 320))   # 改變尺寸和視窗相同
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 轉換成 RGB
        height, width, channel = frame.shape    # 讀取尺寸和 channel數量
        bytesPerline = channel * width          # 設定 bytesPerline ( 轉換使用 )
        # 轉換影像為 QImage，讓 PyQt 可以讀取
        img = QImage(frame, width, height, bytesPerline, QImage.Format.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(img)) # QLabel 顯示影像

video = threading.Thread(target=opencv)         # 建立 OpenCV 的 Thread
video.start()                                   # 啟動 Thread

MainWindow.show()
sys.exit(app.exec())

