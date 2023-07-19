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
        # self.action_open = QtWidgets.QAction('Open')   # PyQt5 寫法
        self.menu_file.addAction(self.action_open)

        self.action_close = QtGui.QAction('Close')
        # self.action_close = QtWidgets.QAction('Close') # PyQt5 寫法
        self.menu_file.addAction(self.action_close)

        self.menu_sub = QtWidgets.QMenu('More')      # 建立 More 選項 ( QMenu )
        self.action_A = QtGui.QAction('A')           # 建立 A 選項 ( QAction )
        self.action_B = QtGui.QAction('B')           # 建立 B 選項 ( QAction )
        # self.action_A = QtWidgets.QAction('A')     # PyQt5 寫法
        # self.action_B = QtWidgets.QAction('B')     # PyQt5 寫法
        self.menu_sub.addActions([self.action_A, self.action_B])   # More 選項中加入 A 和 B
        self.menu_file.addMenu(self.menu_sub)        # 將 More 選項放入 File 選項裡

        self.menubar.addMenu(self.menu_file)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

