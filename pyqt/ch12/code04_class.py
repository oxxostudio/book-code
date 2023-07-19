# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor, QPen
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)

    def paintEvent(self, event):
        self.qpainter = QPainter()
        self.qpainter.begin(self)

        self.qpainter.setPen(QPen(QColor('#ff0000'), 5))
        self.qpainter.drawRect(10,10,100,100)

        self.qpainter.setPen(QPen(QColor('#00aa00'), 5))
        self.qpainter.drawEllipse(50, 50, 100, 100)

        self.qpainter.setPen(QPen(QColor('#000000'), 5))
        self.qpainter.drawLine(100,100,300,200)

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

