# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)

    # 定義 paintEvent 屬性，注意需要包含 self 和 event 參數
    def paintEvent(self, event):
        self.qpainter = QPainter()
        self.qpainter.begin(self)

        self.qpainter.setPen(QColor('#ff0000'))
        self.qpainter.drawText(50,50,'hello')   # 在 (50,50) 的位置加入文字

        self.qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

