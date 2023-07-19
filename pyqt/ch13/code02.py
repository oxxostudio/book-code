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

label = QtWidgets.QLabel(MainWindow)
label.setGeometry(0, 0, 300, 200)

qpixmap = QPixmap()
qimg = QImage('mona.jpg')            # 讀取圖片
qpixmap = qpixmap.fromImage(qimg)    # 將圖片加入 QPixmap 物件中
label.setPixmap(qpixmap)             # 將 QPixmap 物件加入到 label 裡
MainWindow.show()
sys.exit(app.exec())



