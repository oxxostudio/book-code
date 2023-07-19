# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

box = QtWidgets.QWidget(Form)        # 建立放 QGridLayout 的元件
box.setGeometry(10,10,150,150)       # 指定大小位置

grid = QtWidgets.QGridLayout(box)    # 建立 QGridLayout

btn1 = QtWidgets.QPushButton(Form)   # 建立按鈕
btn1.setText('1')
grid.addWidget(btn1, 0, 0)           # 按鈕放在 (0, 0) 位置

btn2 = QtWidgets.QPushButton(Form)   # 建立按鈕
btn2.setText('2')
grid.addWidget(btn2, 0, 1)           # 按鈕放在 (0, 1) 位置

btn3 = QtWidgets.QPushButton(Form)   # 建立按鈕
btn3.setText('3')
grid.addWidget(btn3, 0, 2)           # 按鈕放在 (0, 2) 位置

btn4 = QtWidgets.QPushButton(Form)   # 建立按鈕
btn4.setText('4')
grid.addWidget(btn4, 1, 0)           # 按鈕放在 (1, 0) 位置

btn5 = QtWidgets.QPushButton(Form)   # 建立按鈕
btn5.setText('5')
grid.addWidget(btn5, 1, 1)           # 按鈕放在 (1, 1) 位置

btn6 = QtWidgets.QPushButton(Form)   # 建立按鈕
btn6.setText('6')
grid.addWidget(btn6, 1, 2)           # 按鈕放在 (1, 2) 位置

Form.show()
sys.exit(app.exec())

