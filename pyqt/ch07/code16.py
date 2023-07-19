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
    mbox.addButton('Apple', mbox.ButtonRole.ActionRole)
    mbox.addButton('Banana', mbox.ButtonRole.ActionRole)
    mbox.addButton('Orange', mbox.ButtonRole.ActionRole)
    # mbox.addButton('Apple', 3)   # PyQt5 寫法
    # mbox.addButton('Banana', 3)  # PyQt5 寫法
    # mbox.addButton('Orange', 3)  # PyQt5 寫法
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

