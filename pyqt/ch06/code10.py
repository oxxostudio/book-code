# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

d1 = QtWidgets.QDateEdit(Form)
d1.setGeometry(20,20,100,30)
d1.setDisplayFormat('dd/MM/yyyy')
d1.setDateRange(QtCore.QDate(2000, 1, 1), QtCore.QDate(2000, 2, 1))  # 設定日期範圍

Form.show()
sys.exit(app.exec())

