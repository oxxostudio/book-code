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
        self.input = QtWidgets.QTextEdit(self)         # QTextEdit 多行輸入框
        self.input.setGeometry(20,20,200,100)

        self.input_p = QtWidgets.QPlainTextEdit(self)  # QPlainTextEdit 多行輸入框
        self.input_p.setGeometry(20,130,200,100)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
