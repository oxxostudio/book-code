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
        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(20,20,100,20)
        self.input.textChanged.connect(self.showText)   # 文字改變時執行函式

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20,50,100,20)

    def showText(self):
        self.label.setText(self.input.text())  # 顯示文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

