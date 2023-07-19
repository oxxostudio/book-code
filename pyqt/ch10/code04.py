# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,20,100,30)

def key(self):
    keycode = self.key()         # 取得該按鍵的 keycode
    label.setText(str(keycode))  # QLabel 印出 keycode

Form.keyPressEvent = key         # 建立按下鍵盤事件，對應到 key 函式

Form.show()
sys.exit(app.exec())

