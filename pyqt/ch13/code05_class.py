# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.ui()

    def ui(self):
        grview = QtWidgets.QGraphicsView(self)
        gw = 300
        gh = 300
        grview.setGeometry(0, 0, gw, gh)      # QGraphicsView 的長寬改成變數
        scene = QtWidgets.QGraphicsScene()
        img = QPixmap('mona.jpg')
        img_w = 120                           # 顯示圖片的寬度
        img_h = 160                           # 顯示圖片的高度
        img = img.scaled(img_w, img_h)        # 改變圖片尺寸
        x = 20                                # 左上角 x 座標
        y = 20                                # 左上角 y 座標
        dx = int((gw - img_w) / 2) - x        # 修正公式
        dy = int((gh - img_h) / 2) - y
        scene.setSceneRect(dx, dy, img_w, img_h)
        scene.addPixmap(img)
        grview.setScene(scene)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

