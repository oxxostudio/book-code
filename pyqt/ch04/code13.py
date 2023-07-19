# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

def show(e):
    label.setText(e)   # 顯示參數內容

label = QtWidgets.QLabel(Form)
label.setText('A')
label.setStyleSheet('font-size:20px;')
label.setGeometry(50,30,100,30)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('A')
btn1.setGeometry(50,60,50,30)
btn1.clicked.connect(lambda:show('A'))  # 使用 lambda 函式

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('B')
btn2.setGeometry(110,60,50,30)
btn2.clicked.connect(lambda:show('B'))  # 使用 lambda 函式

Form.show()
sys.exit(app.exec())
