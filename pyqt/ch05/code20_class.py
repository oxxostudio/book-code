# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10,10,200,30)
        self.box = QtWidgets.QComboBox(self)
        self.box.addItems(['A','B','C','D'])
        self.box.setGeometry(10,50,200,30)
        self.box.currentIndexChanged.connect(self.showText)  # 執行函式

    def showText(self):
        text = self.box.currentText()       # 取得目前的文字
        num = self.box.currentIndex()       # 取得編號
        self.label.setText(f'{num}:{text}') # 顯示編號和文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

