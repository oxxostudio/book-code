# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import *     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 200)

label = QtWidgets.QLabel(MainWindow)    # 放入 QLabel
label.setGeometry(0, 0, 300, 200)       # 設定 QLabel 尺寸和位置

qpixmap = QPixmap()                     # 建立 QPixmap 物件
qpixmap.load('mona.jpg')                # 讀取圖片
# 也可以寫成下面這樣
# qpixmap = QPixmap('mona.jpg')
label.setPixmap(qpixmap)                # 將 QPixmap 物件加入到 label 裡

MainWindow.show()
sys.exit(app.exec())

