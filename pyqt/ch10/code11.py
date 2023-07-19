# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui, QtCore  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setText('測試文字')
label.setStyleSheet('font-size:20px;')
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText('開啟新視窗')
btn.setStyleSheet('font-size:16px;')
btn.setGeometry(40,60,120,40)
btn.clicked.connect(lambda:Form2.show())  # 使用 lambda 函式，顯示新視窗

Form2 = QtWidgets.QWidget()               # 建立新視窗
Form2.setWindowTitle('oxxo.studio.2')
Form2.resize(300, 200)

btn2 = QtWidgets.QPushButton(Form2)
btn2.setText('test')
btn2.setGeometry(110,60,50,30)

Form.show()
sys.exit(app.exec())

