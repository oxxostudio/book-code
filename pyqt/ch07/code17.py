# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText('hello')
    a = mbox.addButton('Apple', mbox.ButtonRole.ActionRole)   # 前方多了變數 a
    b = mbox.addButton('Banana', mbox.ButtonRole.ActionRole)  # 前方多了變數 b
    c = mbox.addButton('Orange', mbox.ButtonRole.ActionRole)  # 前方多了變數 c
    # a = mbox.addButton('Apple',3)   # PyQt5 寫法
    # b = mbox.addButton('Banana',3)  # PyQt5 寫法
    # c = mbox.addButton('Orange',3)  # PyQt5 寫法
    mbox.setDefaultButton(b)        # 預先選取 b
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

