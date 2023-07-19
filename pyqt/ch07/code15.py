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
    # 添加三顆按鈕
    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel)
    # mbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)  # PyQt5 寫法
    # 設定預設按鈕
    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
    # mbox.setDefaultButton(QtWidgets.QMessageBox.Yes)  # PyQt5 寫法
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

