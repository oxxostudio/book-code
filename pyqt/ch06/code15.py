# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

slider = QtWidgets.QSlider(Form)
slider.setGeometry(20,20,200,30)
slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
# slider.setOrientation(1)   # PyQt5 寫法
slider.setStyleSheet('''
    QSlider {
        border-radius: 10px;
    }
    QSlider::groove:horizontal {
        height: 5px;
        background: #000;
    }
    QSlider::handle:horizontal{
        background: #f00;
        width: 16px;
        height: 16px;
        margin:-6px 0;
        border-radius:8px;
    }
    QSlider::sub-page:horizontal{
        background:#f90;
    }
''')

Form.show()
sys.exit(app.exec())

