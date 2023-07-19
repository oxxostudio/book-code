# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def show():
    text, ok = QtWidgets.QInputDialog().getText(Form, '', '請輸入一段文字')  # 建立輸入視窗
    label.setText(text)    # 顯示文字

label = QtWidgets.QLabel(Form)
label.setGeometry(10,50,200,50)
label.setStyleSheet('font-size:30px;')

btn = QtWidgets.QPushButton(Form)
btn.setGeometry(10,10,100,30)
btn.setText('輸入')
btn.clicked.connect(show)   # 執行開啟輸入視窗函式

Form.show()
sys.exit(app.exec())

