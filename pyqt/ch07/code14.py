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
    mbox.addButton(QtWidgets.QMessageBox.StandardButton.Ok)
    mbox.addButton(QtWidgets.QMessageBox.StandardButton.Open)
    mbox.addButton(QtWidgets.QMessageBox.StandardButton.Save)
    mbox.addButton(QtWidgets.QMessageBox.StandardButton.Cancel)
    # mbox.addButton(QtWidgets.QMessageBox.Ok)      # PyQt5 寫法
    # mbox.addButton(QtWidgets.QMessageBox.Open)    # PyQt5 寫法
    # mbox.addButton(QtWidgets.QMessageBox.Save)    # PyQt5 寫法
    # mbox.addButton(QtWidgets.QMessageBox.Cancel)  # PyQt5 寫法
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

