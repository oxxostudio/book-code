# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

a = 0                           # a 預設 0
def show():
    global a                    # 定義 a 使用全域變數
    a = a + 1                   # 每次執行時讓 a 增加 1
    label.setText(str(a))       # 更新 QLabel 內容

label = QtWidgets.QLabel(Form)
label.setText('0')
label.setStyleSheet('font-size:20px;')
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText('增加數字')
btn.setGeometry(50,60,100,30)
btn.clicked.connect(show)       # 點擊時執行 show 函式

Form.show()
sys.exit(app.exec())
