# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 300)

grview = QtWidgets.QGraphicsView(MainWindow)  # 加入 QGraphicsView
grview.setGeometry(0, 0, 300, 300)            # 設定 QGraphicsView 位置與大小
scene = QtWidgets.QGraphicsScene()            # 加入 QGraphicsScene
scene.setSceneRect(0, 0, 200, 200)            # 設定 QGraphicsScene 位置與大小
img = QPixmap('mona.jpg')                     # 加入圖片
scene.addPixmap(img)                          # 將圖片加入 scene
grview.setScene(scene)                        # 設定 QGraphicsView 的場景為 scene

MainWindow.show()
sys.exit(app.exec())

