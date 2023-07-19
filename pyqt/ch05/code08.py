# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(360, 300)

input = QtWidgets.QPlainTextEdit(Form)
input.setGeometry(20,20,200,100)
input.setStyleSheet('''
    QPlainTextEdit {
        border:1px solid #000;
        background:#ccc;
        color:#f00;
    }
    QPlainTextEdit:focus {
        border:3px solid #09c;
        background:#fff;
    }
''')

Form.show()
sys.exit(app.exec())
