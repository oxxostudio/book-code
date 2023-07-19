# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)

    def paintEvent(self, event):
        qpainter = QPainter()       # 建立 qpainter 物件
        qpainter.begin(self)        # 開始繪圖

        qimage = QImage('mona.jpg') # 建立圖片物件
        w = qimage.size().width()   # 取得圖片寬度
        h = qimage.size().height()  # 取得圖片高度
        qpainter.drawImage(QRect(20, 20, w, h), qimage)  # 放入圖片

        qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

