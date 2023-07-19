# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('測試文字')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('開啟新視窗')
        self.btn.setStyleSheet('font-size:16px;')
        self.btn.setGeometry(40,60,120,40)
        self.btn.clicked.connect(self.showNewWindow)        # 點擊按鈕，開啟新視窗

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('在新視窗裡顯示文字')
        self.btn2.setStyleSheet('font-size:16px;')
        self.btn2.setGeometry(40,100,200,40)
        self.btn2.clicked.connect(self.changeNewWindowText) # 點擊按鈕，改變新視窗裡的文字

    def showNewWindow(self):
        self.nw = newWindow()
        self.nw.show()
        x = self.nw.pos().x()
        y = self.nw.pos().y()
        self.nw.move(x+50, y+50)
        self.nw.btn.clicked.connect(self.changeText)        # 點擊按鈕，改變主視窗裡的文字

    def changeText(self):
        self.label.setText('點擊按鈕囉')

    def changeNewWindowText(self):
        self.nw.label.setText('主視窗也點擊按鈕囉')

class newWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio.2')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,200,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('test')
        self.btn.setStyleSheet('font-size:16px;')
        self.btn.setGeometry(40,60,120,40)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

