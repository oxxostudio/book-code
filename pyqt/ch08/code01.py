# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

# 垂直 Layout

vbox = QtWidgets.QWidget(Form)         # 建立一個新的 Widget
vbox.setGeometry(0,0,150,150)          # 設定 Widget 大小

v_layout = QtWidgets.QVBoxLayout(vbox) # 建立垂直 Layout

btn1 = QtWidgets.QPushButton(Form)     # 在視窗中加入一個 QPushButton
btn1.setText('1')                      # 按鈕文字
v_layout.addWidget(btn1)               # 將按鈕放入 v_layout 中

btn2 = QtWidgets.QPushButton(Form)     # 在視窗中加入一個 QPushButton
btn2.setText('2')                      # 按鈕文字
v_layout.addWidget(btn2)               # 將按鈕放入 v_layout 中

btn3 = QtWidgets.QPushButton(Form)     # 在視窗中加入一個 QPushButton
btn3.setText('3')                      # 按鈕文字
v_layout.addWidget(btn3)               # 將按鈕放入 v_layout 中

# 水平 Layout

hbox = QtWidgets.QWidget(Form)         # 建立一個新的 Widget
hbox.setGeometry(150,0,150,150)        # 設定 Widget 大小

h_layout = QtWidgets.QHBoxLayout(hbox) # 建立水平 Layout

btn4 = QtWidgets.QPushButton(Form)     # 在視窗中加入一個 QPushButton
btn4.setText('4')                      # 按鈕文字
h_layout.addWidget(btn4)               # 將按鈕放入 h_layout 中

btn5 = QtWidgets.QPushButton(Form)     # 在視窗中加入一個 QPushButton
btn5.setText('5')                      # 按鈕文字
h_layout.addWidget(btn5)               # 將按鈕放入 h_layout 中

btn6 = QtWidgets.QPushButton(Form)     # 在視窗中加入一個 QPushButton
btn6.setText('6')                      # 按鈕文字
h_layout.addWidget(btn6)               # 將按鈕放入 h_layout 中

Form.show()
sys.exit(app.exec())

