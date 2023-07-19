# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label1 = QtWidgets.QLabel('AAA')
input1 = QtWidgets.QLineEdit(Form)
label2 = QtWidgets.QLabel('BBB')
input2 = QtWidgets.QLineEdit(Form)
label3 = QtWidgets.QLabel('CCC')
input3 = QtWidgets.QPlainTextEdit(Form)

box = QtWidgets.QWidget(Form)          # 建立放置 QFormLayout 的 Widget
box.setGeometry(10,10,200,150)

layout = QtWidgets.QFormLayout(box)    # 建立 QFormLayout
layout.addRow(label1, input1)          # QFormLayout 加入一列，內容為文字 + 輸入框
layout.addRow(label2, input2)          # QFormLayout 加入一列，內容為文字 + 輸入框
layout.addRow(label3, input3)          # QFormLayout 加入一列，內容為文字 + 輸入框

Form.show()
sys.exit(app.exec())
