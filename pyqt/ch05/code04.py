# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

input_1 = QtWidgets.QLineEdit(Form)
input_1.setGeometry(20,20,100,20)
input_1.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # 設定密碼輸入
input_1.setText('12345')  # 預設文字 12345
input_1.setMaxLength(5)   # 最多五個字元

input_2 = QtWidgets.QLineEdit(Form)
input_2.setGeometry(20,50,100,20)
input_2.setFocus()        # 設定焦點

Form.show()
sys.exit(app.exec())
