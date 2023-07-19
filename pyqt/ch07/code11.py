# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show(n):
    mbox = QtWidgets.QMessageBox(Form)  # 建立對話視窗
    if n==1:
      mbox.information(Form, 'information', 'information...') # information 視窗
    elif n == 2:
      mbox.question(Form, 'question', 'question?')  # question 視窗

    elif n == 3:
      mbox.warning(Form, 'warning', 'warning!!!')   # warning 視窗

    elif n == 4:
      mbox.critical(Form, 'critical', 'critical!!!')   # critical 視窗

btn1 = QtWidgets.QPushButton(Form)
btn1.move(10, 10)
btn1.setText('information')
btn1.clicked.connect(lambda: show(1)) # 使用 1 為參數內容執行函式

btn2 = QtWidgets.QPushButton(Form)
btn2.move(10, 40)
btn2.setText('question')
btn2.clicked.connect(lambda: show(2)) # 使用 2 為參數內容執行函式

btn3 = QtWidgets.QPushButton(Form)
btn3.move(10, 70)
btn3.setText('waring')
btn3.clicked.connect(lambda: show(3)) # 使用 3 為參數內容執行函式

btn4 = QtWidgets.QPushButton(Form)
btn4.move(10, 100)
btn4.setText('critical')
btn4.clicked.connect(lambda: show(4)) # 使用 4 為參數內容執行函式

Form.show()
sys.exit(app.exec())

