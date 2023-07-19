# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    items = ['a','b','c','d','e']
    item, ok = QtWidgets.QInputDialog().getItem(Form, '', '請選擇一個選項', items, 0)
    label.setText(item)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,50,200,50)
label.setStyleSheet('font-size:30px;')

btn = QtWidgets.QPushButton(Form)
btn.setGeometry(10,10,100,30)
btn.setText('開啟選項')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

