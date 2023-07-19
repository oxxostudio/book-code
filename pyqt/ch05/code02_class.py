# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.input_1 = QtWidgets.QLineEdit(self)   # 第一個輸入框
        self.input_1.move(20,20)                   # 移動到 (20, 20)

        self.input_2 = QtWidgets.QLineEdit(self)   # 第二個輸入框
        self.input_2.setGeometry(20,50,100,20)     # 設定位置與長寬

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
