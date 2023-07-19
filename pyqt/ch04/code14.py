# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

rb_a = QtWidgets.QRadioButton(Form)    # 單選按鈕 A
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText('A')

rb_b = QtWidgets.QRadioButton(Form)    # 單選按鈕 B
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText('B')

Form.show()
sys.exit(app.exec())
