# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore, QtWebEngineWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(800, 600)
        self.web()
        self.ui()

    def web(self):
        self.widget = QtWebEngineWidgets.QWebEngineView(self)
        self.widget.move(0,60)
        self.widget.resize(800, 540)
        self.widget.load(QtCore.QUrl('https://google.com'))
        self.widget.loadFinished.connect(self.finished)
        self.widget.selectionChanged.connect(self.show)

    def ui(self):
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setGeometry(10,10,80,30)
        self.btn1.setText('重新整理')
        self.btn1.clicked.connect(lambda: self.widget.reload())

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(100,10,80,30)
        self.btn2.setText('下一頁')
        self.btn2.clicked.connect(lambda: self.widget.forward())

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.setGeometry(190,10,80,30)
        self.btn3.setText('上一頁')
        self.btn3.clicked.connect(lambda: self.widget.back())

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.setGeometry(280,10,80,30)
        self.btn4.setText('停止')
        self.btn4.clicked.connect(lambda: self.widget.stop())

        self.btn5 = QtWidgets.QPushButton(self)
        self.btn5.setGeometry(600,10,80,30)
        self.btn5.setText('前往')
        self.btn5.clicked.connect(self.go)

        self.input = QtWidgets.QLineEdit(self)
        self.input.setGeometry(400,10,200,30)

    def go(self):
        url = self.input.text()
        self.widget.load(QtCore.QUrl(url))

    def finished(self):
        self.setWindowTitle(self.widget.title())
        self.setWindowIcon(self.widget.icon())

    def showMsg(self):
        print(self.widget.selectedText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

