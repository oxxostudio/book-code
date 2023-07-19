# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    label.setText(input.text())   # 顯示文字

input = QtWidgets.QLineEdit(Form)
input.setGeometry(20,20,100,20)
input.textChanged.connect(show)   # 文字改變時執行函式

label = QtWidgets.QLabel(Form)
label.setGeometry(20,50,100,20)

Form.show()
sys.exit(app.exec())

