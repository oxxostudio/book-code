# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.menubar = QtWidgets.QMenuBar(self)

        self.menu_file = QtWidgets.QMenu('File')

        self.action_open = QtGui.QAction('Open')
        # self.action_open = QtWidgets.QAction('Open') # PyQt5 寫法
        self.menu_file.addAction(self.action_open)

        self.menu_file.addSeparator()    # 加入分隔線

        self.action_close = QtGui.QAction('Close')
        # self.action_close = QtWidgets.QAction('Close') # PyQt5 寫法
        self.menu_file.addAction(self.action_close)

        self.menubar.addMenu(self.menu_file)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

