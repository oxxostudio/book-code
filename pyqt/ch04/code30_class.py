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
        self.grview = QtWidgets.QGraphicsView(self)   # 加入 QGraphicsView
        self.grview.setGeometry(0, 0, 300, 300)       # 設定 QGraphicsView 位置與大小
        scene = QtWidgets.QGraphicsScene()            # 加入 QGraphicsScene
        scene.setSceneRect(0, 0, 200, 200)            # 設定 QGraphicsScene 位置與大小
        img = QtGui.QPixmap('mona.jpg')               # 建立圖片
        img1 = img.scaled(200,50)                     # 建立不同尺寸圖片
        qitem1 = QtWidgets.QGraphicsPixmapItem(img1)  # 設定 QItem，內容是 img1
        img2 = img.scaled(100,150)                    # 建立不同尺寸圖片
        qitem2 = QtWidgets.QGraphicsPixmapItem(img2)  # 設定 QItem，內容是 img2
        scene.addItem(qitem1)                         # 場景中加入 QItem
        scene.addItem(qitem2)                         # 場景中加入 QItem
        self.grview.setScene(scene)                  # 設定 QGraphicsView 的場景為 scene

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
