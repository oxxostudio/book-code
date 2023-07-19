# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20, 20, 200, 150)

        img = QtGui.QImage('mona.jpg')                      # 讀取圖片
        self.label.setPixmap(QtGui.QPixmap.fromImage(img))  # 加入圖片

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
