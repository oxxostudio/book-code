# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

def show():
    mbox = QtWidgets.QMessageBox(Form)       # 加入對話視窗
    mbox.information(Form, 'info', 'hello')  # 開啟資訊通知的對話視窗，標題 info，內容 hello

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('彈出視窗')
btn.clicked.connect(show)   # 點擊按鈕執行函式

Form.show()
sys.exit(app.exec())

