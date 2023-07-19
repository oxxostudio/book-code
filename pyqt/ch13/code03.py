# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)  #  建立 QLabel
label.setGeometry(0, 0, 300, 200)
label2 = QtWidgets.QLabel(MainWindow) #  建立 QLabel
label2.setGeometry(0, 0, 300, 200)
label2.move(0, -50)                   # 調整位置

qpixmap = QPixmap()
qpixmap.load('mona.jpg')
img1 = qpixmap.scaled(300,50)    # 建立圖片 1
label.setPixmap(img1)            # 加入圖片 1
img2 = qpixmap.scaled(150,200)   # 建立圖片 2
label2.setPixmap(img2)           # 加入圖片 2
MainWindow.show()
sys.exit(app.exec())

