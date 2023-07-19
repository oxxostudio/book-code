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
        self.menubar = QtWidgets.QMenuBar(self)     # 建立 menubar

        self.menu_file = QtWidgets.QMenu('File')    # 建立一個 File 選項 ( QMenu )

        self.action_open = QtGui.QAction('Open')    # 建立一個 Open 選項 ( QAction )
        # self.action_open = QtWidgets.QAction('Open')  # PyQt5 寫法 - 建立一個 Open 選項 ( QAction )
        self.menu_file.addAction(self.action_open)  # 將 Open 選項放入 File 選項裡

        self.action_close = QtGui.QAction('Close')  # 建立一個 Close 選項 ( QAction )
        # self.action_close = QtWidgets.QAction('Close')  # PyQt5 寫法 - 建立一個 Open 選項 ( QAction )
        self.menu_file.addAction(self.action_close) # 將 Close 選項放入 File 選項裡

        self.menubar.addMenu(self.menu_file)        # 將 File 選項放入 menubar 裡

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

