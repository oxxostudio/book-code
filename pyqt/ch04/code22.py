# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

cb_a = QtWidgets.QCheckBox(Form)    # 複選按鈕 A
cb_a.setGeometry(30, 60, 50, 20)    # 設定位置
cb_a.setText('A')                   # 設定文字

cb_b = QtWidgets.QCheckBox(Form)    # 複選按鈕 B
cb_b.setGeometry(80, 60, 50, 20)    # 設定位置
cb_b.setText('B')                   # 設定文字

cb_c = QtWidgets.QCheckBox(Form)    # 複選按鈕 C
cb_c.setGeometry(130, 60, 50, 20)   # 設定位置
cb_c.setText('C')                   # 設定文字

Form.show()
sys.exit(app.exec())
