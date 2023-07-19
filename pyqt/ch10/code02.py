# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets       # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QCursor   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,100,50)
label.setStyleSheet('font-size:24px;')

def mouseMove(self):
    mx = QCursor.pos().x() - Form.x()
    my= QCursor.pos().y() - Form.y()
    label.setText(f'{mx}, {my}')   # 透過 QLabel 顯示滑鼠座標

Form.setMouseTracking(True)        # 設定不需要按下滑鼠，就能偵測滑鼠移動
Form.mouseMoveEvent  = mouseMove   # 滑鼠移動事件發生時，執行 mouseMove 函式

Form.show()
sys.exit(app.exec())

