# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui, QtCore     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

box = QtWidgets.QComboBox(Form)
box.addItems(['A','B','C','D'])
box.setGeometry(10,10,200,30)

box.addItem('apple')     # 在最後方添加 apple 選項
box.removeItem(2)        # 移除第三個選項 C
box.insertItem(0, 'ok')  # 在最前方加入 ok 為第一個選項

Form.show()
sys.exit(app.exec())

