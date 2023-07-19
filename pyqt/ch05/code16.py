# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)   # 加入下拉選單
box.addItems(['A','B','C','D'])   # 加入四個選項
box.setGeometry(10,10,200,30)

Form.show()
sys.exit(app.exec())

