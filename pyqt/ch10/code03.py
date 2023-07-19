# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets            # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QEnterEvent    # PyQt5 不用這行
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,200,50)
label.setStyleSheet('font-size:24px;')

def mousePress(self):
    m = QEnterEvent.button(self)
    t = QEnterEvent.timestamp(self)
    # m = self.button()     # PyQt5 寫法
    # t = self.timestamp()  # PyQt5 寫法
    print(m,t)   # 印出按下了滑鼠的哪個鍵

def mouseMove(self):
    mx = QEnterEvent.position(self).x()
    my= QEnterEvent.position(self).y()
    mx = self.globalX()  # PyQt5 寫法
    my= self.globalY()   # PyQt5 寫法
    label.setText(f'{mx}, {my}')   # 透過 QLabel 顯示滑鼠座標

Form.setMouseTracking(True)          # 設定不需要按下滑鼠，就能偵測滑鼠移動
Form.mouseMoveEvent  = mouseMove     # 滑鼠移動事件發生時，執行 mouseMove 函式
Form.mousePressEvent  = mousePress   # 滑鼠按下事件發生時，執行 mousePress 函式

Form.show()
sys.exit(app.exec())

