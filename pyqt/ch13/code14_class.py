# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys, cv2

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.setUpdatesEnabled(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.setGeometry(0,0,300,300)
        img = cv2.imread('mona.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        bytesPerline = channel * width
        qimg = QImage(img, width, height, bytesPerline, QImage.Format.Format_RGB888)
        # qimg = QImage(img, width, height, bytesPerline, QImage.Format_RGB888) # PyQt5 寫法
        canvas = QPixmap(300,300).fromImage(qimg)
        self.label.setPixmap(canvas)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

