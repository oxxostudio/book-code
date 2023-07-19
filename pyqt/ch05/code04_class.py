# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.input_1 = QtWidgets.QLineEdit(self)
        self.input_1.setGeometry(20,20,100,20)
        self.input_1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # 設定密碼輸入
        self.input_1.setText('12345')  # 預設文字 12345
        self.input_1.setMaxLength(5)   # 最多五個字元

        self.input_2 = QtWidgets.QLineEdit(self)
        self.input_2.setGeometry(20,50,100,20)
        self.input_2.setFocus()        # 設定焦點

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

