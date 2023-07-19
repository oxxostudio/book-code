# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

# 設定放置 Layout 的 Widget 樣式
style_box = '''
    background:#fff;
    border:1px solid #000;
'''
# 設定按鈕樣式
style_btn = '''
    QPushButton{
        background:#ff0;
        border:1px solid #000;
        border-radius:10px;
        padding:5px;
    }
    QPushButton:pressed{
        background:#f90;
    }
'''

# 垂直 Layout

vbox = QtWidgets.QWidget(Form)
vbox.setGeometry(0,0,120,120)
vbox.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox)
v_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # 靠左對齊
# v_layout.setAlignment(QtCore.Qt.AlignLeft)  # PyQt5 寫法

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('1')
btn1.setStyleSheet(style_btn)
v_layout.addWidget(btn1)

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('2')
btn2.setStyleSheet(style_btn)
v_layout.addWidget(btn2)

btn3 = QtWidgets.QPushButton(Form)
btn3.setText('3')
btn3.setStyleSheet(style_btn)
v_layout.addWidget(btn3)

# 水平 Layout

hbox = QtWidgets.QWidget(Form)
hbox.setGeometry(130,0,120,120)
hbox.setStyleSheet(style_box)

h_layout = QtWidgets.QHBoxLayout(hbox)
h_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop) # 靠上對齊
# h_layout.setAlignment(QtCore.Qt.AlignTop) # PyQt5 寫法

btn4 = QtWidgets.QPushButton(Form)
btn4.setText('4')
btn4.setStyleSheet(style_btn)
h_layout.addWidget(btn4)

btn5 = QtWidgets.QPushButton(Form)
btn5.setText('5')
btn5.setStyleSheet(style_btn)
h_layout.addWidget(btn5)

btn6 = QtWidgets.QPushButton(Form)
btn6.setText('6')
btn6.setStyleSheet(style_btn)
h_layout.addWidget(btn6)

Form.show()
sys.exit(app.exec())

