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
        self.btn1 = QtWidgets.QPushButton(self)  # 第一個按鈕
        self.btn1.setText('按鈕 1')               # 按鈕文字
        self.btn1.move(50,30)                    # 移動到 (50,30)

        self.btn2 = QtWidgets.QPushButton(self)  # 第二個按鈕
        self.btn2.setText('按鈕 2')              # 按鈕文字
        self.btn2.setGeometry(50,60,100,50)      # 移動到 (50,60)，大小 100x50

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
