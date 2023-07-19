# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)                    # 視窗大小

grview = QtWidgets.QGraphicsView(Form)
grview.setGeometry(20, 20, 260, 200)     # QGraphicsView 位置 (20, 20) 和大小 260x200
scene = QtWidgets.QGraphicsScene()
scene.setSceneRect(0, 0, 120, 160)       # QGraphicsScene 相對位置 (20, 20) 和大小 120x160
img = QtGui.QPixmap('mona.jpg')
img = img.scaled(120,160)                # 調整圖片大小為 120x160
scene.addPixmap(img)
grview.setScene(scene)

Form.show()
sys.exit(app.exec())
