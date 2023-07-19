# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

label = QtWidgets.QLabel(Form)
label.setText('hello world, how are you?')
label.setGeometry(20, 20, 200, 150)
label.setWordWrap(True)    # 設定可以換行

label.setStyleSheet('''
    background:#fff;
    color:#f00;
    font-size:20px;
    font-weight:bold;
    border:2px dashed #000;
    padding:20px;
    text-align:center;
''')

Form.show()
sys.exit(app.exec())
