# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

grview = QtWidgets.QGraphicsView(Form)  # 加入 QGraphicsView
grview.setGeometry(20, 20, 260, 200)    # 設定 QGraphicsView 位置與大小
scene = QtWidgets.QGraphicsScene()      # 加入 QGraphicsScene
scene.setSceneRect(0, 0, 300, 400)      # 設定 QGraphicsScene 位置與大小
img = QtGui.QPixmap('mona.jpg')         # 加入圖片
scene.addPixmap(img)                    # 將圖片加入 scene
grview.setScene(scene)                  # 設定 QGraphicsView 的場景為 scene

Form.show()
sys.exit(app.exec())
