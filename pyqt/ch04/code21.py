# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

def show(rb):
    label.setText(rb.text() + ':' + str(rb.isChecked()))  # 取得按鈕狀態

rb_a = QtWidgets.QRadioButton(Form)       # 建立 QRadioButton A
rb_a.setGeometry(30, 60, 100, 20)
rb_a.setText('A')
rb_a.toggled.connect(lambda: show(rb_a))  # 綁定函式

rb_b = QtWidgets.QRadioButton(Form)       # 建立 QRadioButton B
rb_b.setGeometry(150, 60, 100, 20)
rb_b.setText('B')
rb_b.toggled.connect(lambda: show(rb_b))  # 綁定函式

group = QtWidgets.QButtonGroup(Form)      # 建立群組
group.addButton(rb_a)                     # 添加 QRadioButton A
group.addButton(rb_b)                     # 添加 QRadioButton A

label = QtWidgets.QLabel(Form)
label.setGeometry(30, 30, 100, 20)

Form.show()
sys.exit(app.exec())
