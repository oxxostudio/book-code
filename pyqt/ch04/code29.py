# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

grview = QtWidgets.QGraphicsView(Form)
gw = 260
gh = 200
grview.setGeometry(20, 20, gw, gh)    # QGraphicsView 的長寬改成變數
scene = QtWidgets.QGraphicsScene()
img = QtGui.QPixmap('mona.jpg')
img_w = 120                           # 顯示圖片的寬度
img_h = 160                           # 顯示圖片的高度
img = img.scaled(img_w, img_h)
x = 20                                # 左上角 x 座標
y = 20                                # 左上角 y 座標
dx = int((gw - img_w) / 2) - x        # 修正公式
dy = int((gh - img_h) / 2) - y
scene.setSceneRect(dx, dy, img_w, img_h)
scene.addPixmap(img)
grview.setScene(scene)

Form.show()
sys.exit(app.exec())
