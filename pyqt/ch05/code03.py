# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

input_1 = QtWidgets.QLineEdit(Form)
input_1.move(20,20)
input_1.setStyleSheet('''
    QLineEdit {
        border:1px solid #000;
    }
    QLineEdit:focus {
        border:2px solid #f00;
        background:#ff0;
    }
''')

input_2 = QtWidgets.QLineEdit(Form)
input_2.setGeometry(20,50,100,20)

Form.show()
sys.exit(app.exec())
