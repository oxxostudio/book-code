# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,200,30)


def show():
    text = box.currentText()       # 取得目前的文字
    num = box.currentIndex()       # 取得編號
    label.setText(f'{num}:{text}') # 顯示編號和文字

box = QtWidgets.QComboBox(Form)
box.addItems(['A','B','C','D'])
box.setGeometry(10,50,200,30)
box.currentIndexChanged.connect(show)  # 執行函式

Form.show()
sys.exit(app.exec())

