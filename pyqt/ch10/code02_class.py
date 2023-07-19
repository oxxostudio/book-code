# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets       # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QCursor   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setMouseTracking(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10,10,100,50)
        self.label.setStyleSheet('font-size:24px;')

    def mouseMoveEvent(self, event):
        mx = QCursor.pos().x() - self.x()
        my= QCursor.pos().y() - self.y()
        self.label.setText(f'{mx}, {my}')   # 透過 QLabel 顯示滑鼠座標

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

