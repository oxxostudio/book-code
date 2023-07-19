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
btn.setStyleSheet('''
    QPushButton {
        font-size:20px;
        color: #f00;
        background: #ff0;
        border: 2px solid #000;
    }
    QPushButton:disabled {
        color:#fff;
        background:#ccc;
        border: 2px solid #aaa;
    }
''')
btn.setDisabled(True)

Form.show()
sys.exit(app.exec())
