# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)
box.addItems(['A','B','C','D'])
box.setGeometry(10,10,200,30)
box.setItemIcon(0, QtGui.QIcon('icon.png'))   # 第一個選項
box.setItemIcon(1, QtGui.QIcon('mona.jpg'))   # 第二個選項
box.setItemIcon(2, QtGui.QIcon('orange.jpg')) # 第三個選項
box.setItemIcon(3, QtGui.QIcon('ok.png'))     # 第四個選項

Form.show()
sys.exit(app.exec())

