# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def showInt():
    num, ok = QtWidgets.QInputDialog().getInt(Form, '', '請輸入一個整數')
    label.setText(str(num))

def showDouble():
    num, ok = QtWidgets.QInputDialog().getDouble(Form, '', '請輸入一個浮點數')
    label.setText(str(num))

label = QtWidgets.QLabel(Form)
label.setGeometry(10,50,200,50)
label.setStyleSheet('font-size:30px;')

btn1 = QtWidgets.QPushButton(Form)
btn1.setGeometry(10,10,100,30)
btn1.setText('整數')
btn1.clicked.connect(showInt)

btn2 = QtWidgets.QPushButton(Form)
btn2.setGeometry(110,10,100,30)
btn2.setText('浮點數')
btn2.clicked.connect(showDouble)

Form.show()
sys.exit(app.exec())

