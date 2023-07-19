# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.ui()

    def ui(self):
        self.label1 = QtWidgets.QLabel(self)              # 在視窗上建立第一組 QLabel 元件
        self.label1.setText('hello world, how are you?')  # 放入文字
        self.label1.move(50, 50)                          # 設定位置

        self.label2 = QtWidgets.QLabel(self)              # 在視窗上建立第二組 QLabel 元件
        self.label2.setText('hello world, how are you?')  # 放入文字
        self.label2.setGeometry(50, 80, 100, 100)         # 設定位置和長寬

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
