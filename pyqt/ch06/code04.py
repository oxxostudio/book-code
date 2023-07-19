# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

timeedit = QtWidgets.QTimeEdit(Form)  # 建立時間調整元件
timeedit.setGeometry(20,20,100,30)    # 設定位置和尺寸

Form.show()
sys.exit(app.exec())

