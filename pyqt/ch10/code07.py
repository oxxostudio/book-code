# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

btn1 = QtWidgets.QPushButton(Form)
btn1.setGeometry(10,10,100,30)
btn1.setText('最大化')
btn1.clicked.connect(lambda: Form.showMaximized())  # 最大化

btn2 = QtWidgets.QPushButton(Form)
btn2.setGeometry(110,10,100,30)
btn2.setText('恢復大小')
btn2.clicked.connect(lambda: Form.showNormal())     # 恢復原本大小

btn3 = QtWidgets.QPushButton(Form)
btn3.setGeometry(10,50,100,30)
btn3.setText('移動視窗')
btn3.clicked.connect(lambda: Form.move(100, 100))   # 移動到 (100, 100)

Form.show()
sys.exit(app.exec())

