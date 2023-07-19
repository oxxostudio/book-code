# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

label1 = QtWidgets.QLabel(Form)              # 在視窗上建立第一組 QLabel 元件
label1.setText('hello world, how are you?')  # 放入文字
label1.move(50, 50)                          # 設定位置

label2 = QtWidgets.QLabel(Form)              # 在視窗上建立第二組 QLabel 元件
label2.setText('hello world, how are you?')  # 放入文字
label2.setGeometry(50, 80, 100, 100)         # 設定位置和長寬
Form.show()
sys.exit(app.exec())
