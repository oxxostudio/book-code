# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 30, 300, 170)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('儲存為 jpg')
        self.btn1.setGeometry(20,0,100,30)
        self.btn1.clicked.connect(lambda: self.save('jpg'))   # 綁定儲存的函式

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('儲存為 png')
        self.btn2.setGeometry(120,0,100,30)
        self.btn2.clicked.connect(lambda: self.save('png'))   # 綁定儲存的函式

    def save(self, format):
        if format == 'jpg':
            self.label.pixmap().save('demo.jpg','JPG',90)   # 儲存為 jpg
        else:
            self.label.pixmap().save('demo.png','PNG')      # 儲存為 png

    def paintEvent(self, event):
        canvas = QPixmap(300,170)
        canvas.fill(QColor('#ffdddd'))
        qpainter = QPainter()
        qpainter.begin(canvas)

        qpainter.setPen(QPen(QColor('#ff0000'), 5))
        qpainter.drawRect(10,10,100,100)

        qpainter.setPen(QPen(QColor('#00aa00'), 5))
        qpainter.drawEllipse(50, 50, 100, 100)

        qpainter.setPen(QPen(QColor('#000000'), 5))
        qpainter.drawLine(100,100,300,200)

        qpainter.end()
        self.label.setPixmap(canvas)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

