# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

btn = QtWidgets.QPushButton(Form)   # 在 Form 中加入一個 QPushButton
btn.setText('我是按鈕')              # 按鈕文字

Form.show()
sys.exit(app.exec())
