# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.ui()

    def ui(self):
        self.grview = QtWidgets.QGraphicsView(self)
        self.grview.setGeometry(20, 20, 260, 200)  # QGraphicsView 位置 (20, 20) 和大小 260x200
        scene = QtWidgets.QGraphicsScene()
        scene.setSceneRect(0, 0, 120, 160)         # QGraphicsScene 相對位置 (20, 20) 和大小 120x160
        img = QtGui.QPixmap('mona.jpg')
        img = img.scaled(120,160)                  # 調整圖片大小為 120x160
        scene.addPixmap(img)
        self.grview.setScene(scene)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
