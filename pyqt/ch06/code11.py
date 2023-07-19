# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,20,120,30)

def show():
    label.setText(d1.date().toString())   # 顯示目前日期

d1 = QtWidgets.QDateEdit(Form)
d1.setGeometry(150,20,100,30)
d1.setDisplayFormat('dd/MM/yyyy')
d1.setDate(QtCore.QDate().currentDate())  # 設定日期為目前日期
d1.dateChanged.connect(show)              # 執行函式

Form.show()
sys.exit(app.exec())

