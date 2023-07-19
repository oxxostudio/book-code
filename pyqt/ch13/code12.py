# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PIL import Image, ImageQt

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

img = Image.open('mona.jpg')               # 使用 Pillow 開啟圖片
qimg = ImageQt.toqimage(img)               # 轉換成 QPixmap 格式
canvas = QPixmap(300,300).fromImage(qimg)  # 建立 QPixmap 畫布，讀取圖片
label = QtWidgets.QLabel(MainWindow)       # 建立 QLabel
label.setGeometry(0, 0, 300, 300)          # 設定 QLabel 尺寸位置
label.setPixmap(canvas)                    # QLabel 放入畫布

MainWindow.show()
sys.exit(app.exec())

