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
        self.input_1 = QtWidgets.QPlainTextEdit(self)
        self.input_1.move(20,20)                  # 移動到指定座標

        self.input_2 = QtWidgets.QPlainTextEdit(self)
        self.input_2.setGeometry(20,230,200,50)   # 移動到指定座標並設定長寬

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

