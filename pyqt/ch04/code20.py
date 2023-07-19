# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 60, 100, 20)
rb_a.setText('A')

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(150, 60, 100, 20)
rb_b.setText('B')

def show():
    label.setText(str(group.checkedId()))   # 設定 label 文字為按鈕群組中勾選按鈕的 ID

group = QtWidgets.QButtonGroup(Form)
group.addButton(rb_a, 1)               # 添加 QRadioButton A，ID 設定為 1
group.addButton(rb_b, 2)               # 添加 QRadioButton B，ID 設定為 2
group.buttonClicked.connect(show)      # 綁定點擊事件

label = QtWidgets.QLabel(Form)
label.setGeometry(30, 30, 100, 20)

Form.show()
sys.exit(app.exec())
