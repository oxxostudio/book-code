# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

cb_a = QtWidgets.QCheckBox(Form)    # 複選按鈕 A
cb_a.move(30, 60)
cb_a.setText('A')

cb_b = QtWidgets.QCheckBox(Form)    # 複選按鈕 B
cb_b.move(80, 60)
cb_b.setText('B')

cb_c = QtWidgets.QCheckBox(Form)    # 複選按鈕 C
cb_c.setGeometry(130, 60, 50, 20)
cb_c.setText('C')

cb_d = QtWidgets.QCheckBox(Form)    # 複選按鈕 D
cb_d.setGeometry(180, 60, 50, 20)
cb_d.setText('D')

Form.show()
sys.exit(app.exec())
