# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)      # 加入 QLabel
label.setGeometry(10,10,150,100)    # 設定位置
label.setText('HELLO')              # 設定內容文字
# 設定樣式
label.setStyleSheet('''
        font-size:30px;
        color:red;
    ''')

Form.show()
sys.exit(app.exec())

