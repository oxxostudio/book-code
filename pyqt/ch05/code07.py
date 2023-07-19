# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(360, 300)

input_1 = QtWidgets.QPlainTextEdit(Form)
input_1.move(20,20)                  # 移動到指定座標

input_2 = QtWidgets.QPlainTextEdit(Form)
input_2.setGeometry(20,230,200,50)   # 移動到指定座標並設定長寬

Form.show()
sys.exit(app.exec())

