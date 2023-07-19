# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

rb_a = QtWidgets.QRadioButton(Form)    # 單選按鈕 A
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText('A')

rb_b = QtWidgets.QRadioButton(Form)    # 單選按鈕 B
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText('B')

group1 = QtWidgets.QButtonGroup(Form)  # 按鈕群組
group1.addButton(rb_a)                 # 加入單選按鈕 A
group1.addButton(rb_b)                 # 加入單選按鈕 B

rb_c = QtWidgets.QRadioButton(Form)    # 單選按鈕 C
rb_c.setGeometry(150, 30, 100, 20)
rb_c.setText('C')

rb_d = QtWidgets.QRadioButton(Form)    # 單選按鈕 D
rb_d.setGeometry(150, 60, 100, 20)
rb_d.setText('D')

group2 = QtWidgets.QButtonGroup(Form)  # 按鈕群組
group2.addButton(rb_c)                 # 加入單選按鈕 C
group2.addButton(rb_d)                 # 加入單選按鈕 D

Form.show()
sys.exit(app.exec())
