# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

input = QtWidgets.QTextEdit(Form)         # QTextEdit 多行輸入框
input.setGeometry(20,20,200,100)

input_p = QtWidgets.QPlainTextEdit(Form)  # QPlainTextEdit 多行輸入框
input_p.setGeometry(20,130,200,100)

Form.show()
sys.exit(app.exec())
