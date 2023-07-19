# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

# 垂直 Layout

vbox = QtWidgets.QWidget(Form)
vbox.setGeometry(0,0,150,150)

v_layout = QtWidgets.QVBoxLayout(vbox)                    # 建立垂直 Layout
v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # 靠左對齊
# v_layout.setAlignment(QtCore.Qt.AlignLeft)              # PyQt5 寫法


btn1 = QtWidgets.QPushButton(Form)
btn1.setText('1')
v_layout.addWidget(btn1)

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('2')
v_layout.addWidget(btn2)

btn3 = QtWidgets.QPushButton(Form)
btn3.setText('3')
v_layout.addWidget(btn3)

# 水平 Layout

hbox = QtWidgets.QWidget(Form)
hbox.setGeometry(150,0,150,150)

h_layout = QtWidgets.QHBoxLayout(hbox)                  # 建立水平 Layout
h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop) # 靠上對齊
# h_layout.setAlignment(QtCore.Qt.AlignTop)             # PyQt5 寫法


btn4 = QtWidgets.QPushButton(Form)
btn4.setText('4')
h_layout.addWidget(btn4)

btn5 = QtWidgets.QPushButton(Form)
btn5.setText('5')
h_layout.addWidget(btn5)

btn6 = QtWidgets.QPushButton(Form)
btn6.setText('6')
h_layout.addWidget(btn6)

Form.show()
sys.exit(app.exec())

