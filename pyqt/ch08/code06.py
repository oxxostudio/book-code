# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

style_box = '''
    background:#fff;
    border:1px solid #000;
'''

style_btn = '''
    background:#ff0;
    padding:5px;
    border-radius:4px;
'''

box = QtWidgets.QWidget(Form)
box.setGeometry(10,10,150,150)
box.setStyleSheet(style_box)

grid = QtWidgets.QGridLayout(box)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('1')
btn1.setStyleSheet(style_btn)
grid.addWidget(btn1, 0, 0)

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('2')
grid.addWidget(btn2, 0, 1)

btn3 = QtWidgets.QPushButton(Form)
btn3.setText('3')
grid.addWidget(btn3, 0, 2)

btn4 = QtWidgets.QPushButton(Form)
btn4.setText('4')
grid.addWidget(btn4, 1, 0, 1, 3)

Form.show()
sys.exit(app.exec())

