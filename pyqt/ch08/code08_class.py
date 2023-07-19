# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label1 = QtWidgets.QLabel('AAA')
        self.input1 = QtWidgets.QLineEdit(self)
        self.label2 = QtWidgets.QLabel('BBB')
        self.input2 = QtWidgets.QLineEdit(self)
        self.label3 = QtWidgets.QLabel('CCC')
        self.input3 = QtWidgets.QPlainTextEdit(self)

        self.box = QtWidgets.QWidget(self)  # 建立放置 QFormLayout 的 Widget
        self.box.setGeometry(10,10,200,150)

        self.layout = QtWidgets.QFormLayout(self.box)    # 建立 QFormLayout
        self.layout.addRow(self.label1, self.input1)     # QFormLayout 加入一列，內容為文字 + 輸入框

        self.layout.addRow(self.label2, self.input2)     # QFormLayout 加入一列，內容為文字 + 輸入框
        self.layout.addRow(self.label3, self.input3)     # QFormLayout 加入一列，內容為文字 + 輸入框

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

