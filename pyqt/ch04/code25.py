# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

# 設定 QCheckBox
style = '''
    QCheckBox {
        color: #00f;
    }
    QCheckBox:hover {
        color: #f00;
    }
    QCheckBox:checked {
        color: #fff;
        background: #000;
    }
'''

cb_a = QtWidgets.QCheckBox(Form)
cb_a.move(30, 60)
cb_a.setText('A')
cb_a.setStyleSheet(style)    # 套用 style

cb_b = QtWidgets.QCheckBox(Form)
cb_b.move(80, 60)
cb_b.setText('B')
cb_b.setStyleSheet(style)    # 套用 style

cb_c = QtWidgets.QCheckBox(Form)
cb_c.move(130, 60)
cb_c.setText('C')
cb_c.setStyleSheet(style)    # 套用 style

Form.show()
sys.exit(app.exec())
