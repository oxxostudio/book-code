# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

btn = QtWidgets.QPushButton(Form)
btn.setGeometry(10,10,150,100)
btn.setText('HELLO')
btn.setStyleSheet('border:1px solid #000')  # 設定邊框後，點擊按鈕的效果就會消失

Form.show()
sys.exit(app.exec())

