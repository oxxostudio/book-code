# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import *     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)     # 放入 QLabel
        self.label.setGeometry(0, 0, 300, 200)  # 設定 QLabel 尺寸和位置

        self.qpixmap = QPixmap()                # 建立 QPixmap 物件
        self.qpixmap.load('mona.jpg')           # 讀取圖片
        # 也可以寫成下面這樣
        # self.qpixmap = QPixmap('mona.jpg')
        self.label.setPixmap(self.qpixmap)      # 將 QPixmap 物件加入到 label 裡

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

