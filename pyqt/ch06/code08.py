# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

date = QtWidgets.QDateEdit(Form)  # 建立日期調整元件
date.setGeometry(20,20,100,30)    # 設定位置

Form.show()
sys.exit(app.exec())

