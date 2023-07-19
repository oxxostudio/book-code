# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

menubar = QtWidgets.QMenuBar(Form)

menu_file = QtWidgets.QMenu('File')

action_open = QtGui.QAction('Open')
# action_open = QtWidgets.QAction('Open') # PyQt5 寫法
menu_file.addAction(action_open)

menu_file.addSeparator()    # 加入分隔線

action_close = QtGui.QAction('Close')
# action_close = QtWidgets.QAction('Close') # PyQt5 寫法
menu_file.addAction(action_close)

menubar.addMenu(menu_file)

Form.show()
sys.exit(app.exec())

