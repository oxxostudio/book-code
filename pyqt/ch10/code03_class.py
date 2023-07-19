# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets            # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QEnterEvent    # PyQt5 不用這行
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
        self.label.setGeometry(10,10,200,50)
        self.label.setStyleSheet('font-size:24px;')

    def mousePressEvent(self, event):
        m = QEnterEvent.button(event)
        t = QEnterEvent.timestamp(event)
        # m = event.button()      # PyQt5 寫法
        # t = event.timestamp()   # PyQt5 寫法

        print(m,t)   # 印出按下了滑鼠的哪個鍵

    def mouseMoveEvent(self, event):
        mx = QEnterEvent.position(event).x()
        my= QEnterEvent.position(event).y()
        # mx = event.globalX()   # PyQt5 寫法
        # my= event.globalY()    # PyQt5 寫法
        self.label.setText(f'{mx}, {my}')   # 透過 QLabel 顯示滑鼠座標

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

