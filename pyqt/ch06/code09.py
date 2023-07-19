# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

d1 = QtWidgets.QDateEdit(Form)
d1.setGeometry(20,20,100,30)
d1.setDisplayFormat('dd/MM/yyyy')  # 設定格式 西元年/月/日

d2 = QtWidgets.QDateEdit(Form)
d2.setGeometry(130,20,100,30)
d2.setDisplayFormat('yyyy/MM/dd')  # 設定格式 日/月/西元年

Form.show()
sys.exit(app.exec())

