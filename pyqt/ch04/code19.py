# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

rb_a = QtWidgets.QRadioButton(Form)
rb_a.setGeometry(30, 30, 100, 20)
rb_a.setText('A')
rb_a.setStyleSheet('''
    QRadioButton {
        color: #00f;
    }
    QRadioButton:hover {
        color:#f00;
    }
''')

rb_b = QtWidgets.QRadioButton(Form)
rb_b.setGeometry(30, 60, 100, 20)
rb_b.setText('B')
rb_b.setStyleSheet('''
    QRadioButton {
        color: #00f;
    }
    QRadioButton:hover {
        color:#f00;
    }
    QRadioButton:disabled {
        color:#ccc;
    }
''')
rb_b.setDisabled(True)   # 停用按鈕 B

Form.show()
sys.exit(app.exec())
