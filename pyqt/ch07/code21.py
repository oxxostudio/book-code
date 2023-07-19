# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    text, ok = QtWidgets.QInputDialog().getText(Form, '', '請輸入一段文字')
    print(text, ok)

btn = QtWidgets.QPushButton(Form)
btn.setGeometry(10,10,100,30)
btn.setText('輸入')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

