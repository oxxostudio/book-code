# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText('A')

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText('B')
rb_b.setDisabled(True)   # 停用

rb_c = QtWidgets.QRadioButton(Form)
rb_c.setGeometry(30, 90, 100, 20)
rb_c.setText('C')
rb_c.setChecked(True)    # 預先勾選

Form.show()
sys.exit(app.exec())
