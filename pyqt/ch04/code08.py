# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

btn = QtWidgets.QPushButton(Form)  # 建立按鈕
btn.setText('按鈕')                # 設定按鈕文字
btn.setGeometry(50,50,100,50)      # 設定位置和長寬
# 設定樣式
btn.setStyleSheet('''
    background:#ff0;
    color:#f00;
    font-size:20px;
    border:2px solid #000;
''')

Form.show()
sys.exit(app.exec())
