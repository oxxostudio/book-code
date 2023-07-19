# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

t1 = QtWidgets.QTimeEdit(Form)
t1.setGeometry(20,20,120,30)
t1.setDisplayFormat('hh:mm:ss')
t1.setTimeRange(QtCore.QTime(10, 00, 00), QtCore.QTime(20, 00, 00))  # 設定時間範圍

Form.show()
sys.exit(app.exec())

