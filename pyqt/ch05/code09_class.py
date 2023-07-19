# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(360, 300)
        self.ui()

    def ui(self):
        self.input_1 = QtWidgets.QPlainTextEdit(self)
        self.input_1.setGeometry(20,20,150,200)
        self.input_1.setStyleSheet('''
            QPlainTextEdit {
                border:1px solid #000;
            }
            QPlainTextEdit:focus {
                border:3px solid #09c;
            }
        ''')
        self.input_1.cursorPositionChanged.connect(self.showText)   # 游標改變時，執行 showText 函式

        self.input_2 = QtWidgets.QPlainTextEdit(self)
        self.input_2.setGeometry(180,20,150,200)

    def showText(self):
        n = self.input_1.textCursor().blockNumber()                 # 取得所在行數
        text = self.input_1.document().findBlockByNumber(n).text()  # 取得該行內容
        self.input_2.setPlainText(text)                             # 另外一個輸入框顯示內容

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

