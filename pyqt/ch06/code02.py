# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

box1 = QtWidgets.QSpinBox(Form)  # 加入整數調整元件
box1.move(30,10)
box1.setRange(0,100)             # 數值調整區間
box1.setSingleStep(1)            # 每次調整間隔
box1.setValue(50)                # 預設值

box2 = QtWidgets.QDoubleSpinBox(Form)  # 加入整數調整元件
box2.move(100,10)
box2.setRange(0,100)             # 數值調整區間
box2.setSingleStep(0.2)          # 每次調整間隔
box2.setValue(50)                # 預設值

Form.show()
sys.exit(app.exec())

