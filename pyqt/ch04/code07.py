# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

btn1 = QtWidgets.QPushButton(Form)  # 第一個按鈕
btn1.setText('按鈕 1')              # 按鈕文字
btn1.move(50,30)                    # 移動到 (50,30)

btn2 = QtWidgets.QPushButton(Form)  # 第二個按鈕
btn2.setText('按鈕 2')              # 按鈕文字
btn2.setGeometry(50,60,100,50)      # 移動到 (50,60)，大小 100x50

Form.show()
sys.exit(app.exec())
