# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore, QtWebEngineWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(800, 600)
        self.ui()

    def ui(self):
        self.widget = QtWebEngineWidgets.QWebEngineView(self)  # 建立網頁顯示元件
        self.widget.move(0,0)
        self.widget.resize(800, 600)
        self.widget.load(QtCore.QUrl("https://google.com"))    # 載入網頁

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

