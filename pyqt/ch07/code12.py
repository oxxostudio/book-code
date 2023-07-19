# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText('hello')   # 通知文字
    mbox.exec()             # 執行

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)  # 點擊後執行函式

Form.show()
sys.exit(app.exec())

