# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

bar1 = QtWidgets.QProgressBar(Form)
bar1.move(20,20)
bar1.setRange(0, 100)
bar1.setValue(50)
bar1.setStyleSheet('''
    QProgressBar {
        border: 2px solid #000;
        border-radius: 5px;
        text-align:center;
        height: 50px;
        width:80px;
    }
    QProgressBar::chunk {
        background: #09c;
        width:1px;
    }
''')

bar2 = QtWidgets.QProgressBar(Form)
bar2.move(120,20)
bar2.setRange(0, 100)
bar2.setValue(50)
bar2.setStyleSheet('''
    QProgressBar {
        border: 2px solid #000;
        text-align:center;
        background:#aaa;
        color:#fff;
        height: 15px;
        border-radius: 8px;
        width:150px;
    }
    QProgressBar::chunk {
        background: #333;
        width:1px;
    }
''')

Form.show()
sys.exit(app.exec())

