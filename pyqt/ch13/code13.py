# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PIL import Image, ImageQt, ImageEnhance

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

img = Image.open('mona.jpg')
img = ImageEnhance.Brightness(img).enhance(5) # 提高亮度
img = ImageEnhance.Contrast(img).enhance(5)   # 提高對比

qimg = ImageQt.toqimage(img)
canvas = QPixmap(300,300).fromImage(qimg)
label = QtWidgets.QLabel(MainWindow)
label.setGeometry(0, 0, 300, 300)
label.setPixmap(canvas)

MainWindow.show()
sys.exit(app.exec())

