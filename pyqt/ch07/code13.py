# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    mbox = QtWidgets.QMessageBox(Form)
    mbox.setText('hello?')
    mbox.setIcon(QtWidgets.QMessageBox.Icon.Question)  # 加入問號 icon
    # mbox.setIcon(4)                                  # PyQt5 寫法 1
    # mbox.setIcon(QtWidgets.QMessageBox.Question)     # PyQt5 寫法 2
    mbox.exec()

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('open')
btn.clicked.connect(show)  # 點擊按鈕開啟訊息視窗

Form.show()
sys.exit(app.exec())

