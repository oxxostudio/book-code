# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore, QtWebEngineWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(800, 600)

btn1 = QtWidgets.QPushButton(Form)
btn1.setGeometry(10,10,80,30)
btn1.setText('重新整理')
btn1.clicked.connect(lambda: widget.reload())  # 重新載入網頁

btn2 = QtWidgets.QPushButton(Form)
btn2.setGeometry(100,10,80,30)
btn2.setText('下一頁')
btn2.clicked.connect(lambda: widget.forward())  # 前往上一頁

btn3 = QtWidgets.QPushButton(Form)
btn3.setGeometry(190,10,80,30)
btn3.setText('上一頁')
btn3.clicked.connect(lambda: widget.back())    # 前往下一頁

btn4 = QtWidgets.QPushButton(Form)
btn4.setGeometry(280,10,80,30)
btn4.setText('停止')
btn4.clicked.connect(lambda: widget.stop())    # 停止網頁載入

input = QtWidgets.QLineEdit(Form)    # 建立單行輸入框
input.setGeometry(400,10,200,30)

def go():
    url = input.text()
    widget.load(QtCore.QUrl(url))    # 載入輸入的網址

btn5 = QtWidgets.QPushButton(Form)
btn5.setGeometry(600,10,80,30)
btn5.setText('前往')
btn5.clicked.connect(go)             # 按下前往按鈕，執行 go 函式

def finished():
    Form.setWindowTitle(widget.title())  # 更新視窗標題
    Form.setWindowIcon(widget.icon())    # 更新視窗圖示

def show():
    print(widget.selectedText())         # 印出選取的文字

widget = QtWebEngineWidgets.QWebEngineView(Form)
widget.move(0,60)
widget.resize(800, 540)
widget.load(QtCore.QUrl('https://google.com'))
widget.loadFinished.connect(finished)
widget.selectionChanged.connect(show)

Form.show()
sys.exit(app.exec())

