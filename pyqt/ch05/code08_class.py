# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.ui()

    def ui(self):
        self.input = QtWidgets.QPlainTextEdit(self)
        self.input.setGeometry(20,20,200,100)
        self.input.setStyleSheet('''
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

