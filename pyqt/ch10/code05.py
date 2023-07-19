# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QKeySequence, QShortcut
# from PyQt5.QtGui import QKeySequence  # PyQt5 使用這行
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,20,100,30)

def ctrl_o():
    label.setText('Ctrl + O')

shortcut1 = QShortcut(QKeySequence("Ctrl+O"), Form)  # 偵測 Ctrl + O
# shortcut1 = QtWidgets.QShortcut(QKeySequence("Ctrl+O"), Form)  # PyQt5 寫法
shortcut1.activated.connect(ctrl_o)

def alt_shift_c():
    label.setText('Alt + Shift + C')

shortcut2 = QShortcut(QKeySequence("Alt+Shift+C"), Form)  # 偵測 Alt + Shift + C
# shortcut2 = QtWidgets.QShortcut(QKeySequence("Alt+Shift+C"), Form)  # PyQt5 寫法
shortcut2.activated.connect(alt_shift_c)


Form.show()
sys.exit(app.exec())
