# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets      # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtGui import QKeySequence, QShortcut
# from PyQt5.QtGui import QKeySequence  # PyQt5 使用這行
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setMouseTracking(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20,20,100,30)

        shortcut1 = QShortcut(QKeySequence("Ctrl+O"), self)  # 偵測 Ctrl + O
        # shortcut1 = QtWidgets.QShortcut(QKeySequence("Ctrl+O"), self)  # PyQt5 寫法
        shortcut1.activated.connect(self.ctrl_o)

        shortcut2 = QShortcut(QKeySequence("Alt+Shift+C"), self)  # 偵測 Alt + Shift + C
        # shortcut2 = QtWidgets.QShortcut(QKeySequence("Alt+Shift+C"), self)  # PyQt5 寫法
        shortcut2.activated.connect(self.alt_shift_c)

    def ctrl_o(self):
        self.label.setText('Ctrl + O')

    def alt_shift_c(self):
        self.label.setText('Alt + Shift + C')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

