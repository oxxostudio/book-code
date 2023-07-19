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
        self.rb_a = QtWidgets.QRadioButton(self)    # 單選按鈕 A
        self.rb_a.setGeometry(30, 30, 100, 20)
        self.rb_a.setText('A')

        self.rb_b = QtWidgets.QRadioButton(self)    # 單選按鈕 B
        self.rb_b.setGeometry(30, 60, 100, 20)
        self.rb_b.setText('B')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
