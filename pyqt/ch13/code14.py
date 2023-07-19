# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys, cv2

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

label = QtWidgets.QLabel(MainWindow)     # 建立 QLabel
label.setGeometry(0,0,300,300)           # 設定 QLabel 大小位置

img = cv2.imread('mona.jpg')                 # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 轉換顏色為 RGB
height, width, channel = img.shape           # 取得圖片長寬尺寸和色彩頻道數量
bytesPerline = channel * width               # 計算 bytesPerline
qimg = QImage(img, width, height, bytesPerline, QImage.Format.Format_RGB888) # 轉換成 PyQt6 使用的圖片格式
# qimg = QImage(img, width, height, bytesPerline, QImage.Format_RGB888) # PyQt5 寫法
canvas = QPixmap(300,300).fromImage(qimg)    # 建立 QPixmap 畫布，讀取圖片
label.setPixmap(canvas)                      # 放入畫布

MainWindow.show()
sys.exit(app.exec())

