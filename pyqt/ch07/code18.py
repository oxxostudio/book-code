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
    mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel)
    mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
    ret = mbox.exec()  # 取得點擊的按鈕數字
    if ret == QtWidgets.QMessageBox.StandardButton.Yes:
        print(1)
    elif ret == QtWidgets.QMessageBox.StandardButton.No:
        print(2)
    elif ret == QtWidgets.QMessageBox.StandardButton.Cancel:
        print(3)
    # 下方為 PyQt5 寫法
    # mbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
    # mbox.setDefaultButton(QtWidgets.QMessageBox.Yes)
    # ret = mbox.exec()
    # if ret == QtWidgets.QMessageBox.Yes:
    #     print(1)
    # elif ret == QtWidgets.QMessageBox.No:
    #     print(2)
    # elif ret == QtWidgets.QMessageBox.Cancel:
    #     print(3)

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

