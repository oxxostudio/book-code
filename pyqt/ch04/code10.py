# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

btn = QtWidgets.QPushButton(Form)
btn.setText('按鈕')
btn.setGeometry(50,50,100,50)
btn.setDisabled(True)     # 停用設為 True

Form.show()
sys.exit(app.exec())
