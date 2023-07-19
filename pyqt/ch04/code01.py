# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

label = QtWidgets.QLabel(Form)   # 在 Form 裡加入標籤
label.setText('hello world')     # 設定標籤文字

Form.show()
sys.exit(app.exec())
