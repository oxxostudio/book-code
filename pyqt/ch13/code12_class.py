# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PIL import Image, ImageQt

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        img = Image.open('mona.jpg')               # 使用 Pillow 開啟圖片
        qimg = ImageQt.toqimage(img)               # 轉換成 QPixmap 格式
        self.canvas = QPixmap(300,300).fromImage(qimg)  # 建立 QPixmap 畫布，讀取圖片
        self.label = QtWidgets.QLabel(self)       # 建立 QLabel
        self.label.setGeometry(0, 0, 300, 300)    # 設定 QLabel 尺寸位置
        self.label.setPixmap(self.canvas)         # QLabel 放入畫布

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

