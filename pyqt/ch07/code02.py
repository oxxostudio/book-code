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
# action_open = QtWidgets.QAction('Open')     # PyQt5 寫法
menu_file.addAction(action_open)

action_close = QtGui.QAction('Close')
# action_close = QtWidgets.QAction('Close')   # PyQt5 寫法
menu_file.addAction(action_close)

menu_sub = QtWidgets.QMenu('More')        # 建立 More 選項 ( QMenu )
action_A = QtGui.QAction('A')             # 建立 A 選項 ( QAction )
action_B = QtGui.QAction('B')             # 建立 B 選項 ( QAction )
# action_A = QtWidgets.Action('A')        # PyQt5 寫法
# action_B = QtWidgets.QAction('B')       # PyQt5 寫法
menu_sub.addActions([action_A, action_B]) # More 選項中加入 A 和 B
menu_file.addMenu(menu_sub)               # 將 More 選項放入 File 選項裡

menubar.addMenu(menu_file)

Form.show()
sys.exit(app.exec())

