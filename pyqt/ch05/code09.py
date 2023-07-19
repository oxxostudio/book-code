# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui,QtCore     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(360, 300)

def show():
    n = input_1.textCursor().blockNumber()                 # 取得所在行數
    text = input_1.document().findBlockByNumber(n).text()  # 取得該行內容
    input_2.setPlainText(text)                             # 另外一個輸入框顯示內容

input_1 = QtWidgets.QPlainTextEdit(Form)
input_1.setGeometry(20,20,150,200)
input_1.setStyleSheet('''
    QPlainTextEdit {
        border:1px solid #000;
    }
    QPlainTextEdit:focus {
        border:3px solid #09c;
    }
''')
input_1.cursorPositionChanged.connect(show)   # 游標改變時，執行 show 函式

input_2 = QtWidgets.QPlainTextEdit(Form)
input_2.setGeometry(180,20,150,200)

Form.show()
sys.exit(app.exec())

