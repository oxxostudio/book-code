# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.ui()

    def ui(self):
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(10, 10)
        self.btn1.setText('information')
        self.btn1.clicked.connect(lambda: self.showBox(1)) # 使用 1 為參數內容執行函式

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(10, 40)
        self.btn2.setText('question')
        self.btn2.clicked.connect(lambda: self.showBox(2)) # 使用 2 為參數內容執行函式

        self.btn3 = QtWidgets.QPushButton(self)
        self.btn3.move(10, 70)
        self.btn3.setText('waring')
        self.btn3.clicked.connect(lambda: self.showBox(3)) # 使用 3 為參數內容執行函式

        self.btn4 = QtWidgets.QPushButton(self)
        self.btn4.move(10, 100)
        self.btn4.setText('critical')
        self.btn4.clicked.connect(lambda: self.showBox(4)) # 使用 4 為參數內容執行函式

    def showBox(self, n):
        mbox = QtWidgets.QMessageBox(self)  # 建立對話視窗
        if n==1:
            mbox.information(self, 'information', 'information...') # information 視窗

        elif n == 2:
            mbox.question(self, 'question', 'question?') # question 視窗

        elif n == 3:
            mbox.warning(self, 'warning', 'warning!!!')  # warning 視窗


        elif n == 4:
            mbox.critical(self, 'critical', 'critical!!!') # critical 視窗



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

