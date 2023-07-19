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
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10,50,200,50)
        self.label.setStyleSheet('font-size:30px;')

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setGeometry(10,10,100,30)
        self.btn.setText('開啟選項')
        self.btn.clicked.connect(self.showResult)

    def showResult(self):
        items = ['a','b','c','d','e']
        item, ok = QtWidgets.QInputDialog().getItem(self, '', '請選擇一個選項', items, 0)
        self.label.setText(item)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

