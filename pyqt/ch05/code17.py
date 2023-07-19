# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)
box.addItems(['A','B','C','D'])
box.setGeometry(10,10,200,30)
box.setCurrentIndex(1)     # 預先顯示第二個選項 ( 第一個為 0 )
box.setCurrentText('D')    # 如果選項文字為 D，則顯示 D

Form.show()
sys.exit(app.exec())

