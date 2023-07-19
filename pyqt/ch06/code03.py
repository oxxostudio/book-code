# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,50,30)

def show():
    label.setText(str(box1.value()))  # 顯示調整數值

box1 = QtWidgets.QSpinBox(Form)
box1.move(80,10)
box1.setRange(0,100)
box1.setSingleStep(1)
box1.setValue(50)
box1.valueChanged.connect(show)   # 調整時執行函式

Form.show()
sys.exit(app.exec())

