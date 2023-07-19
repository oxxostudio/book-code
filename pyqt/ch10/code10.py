# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setText('測試文字')
label.setStyleSheet('font-size:20px;')
label.setGeometry(50,30,100,30)

btn = QtWidgets.QPushButton(Form)
btn.setText('開啟新視窗')
btn.setStyleSheet('font-size:16px;')
btn.setGeometry(40,60,120,40)

Form.show()
sys.exit(app.exec())

