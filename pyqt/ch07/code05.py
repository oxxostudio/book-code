# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def open():
    filePath , filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選擇檔案對話視窗
    print(filePath , filterType)

def close():
    print('close')
    app.quit()         # 結束應用程式

menubar = QtWidgets.QMenuBar(Form)

menu_file = QtWidgets.QMenu('File')

action_open = QtGui.QAction('Open')
# action_open = QtWidgets.QAction('Open')   # PyQt5 寫法
action_open.triggered.connect(open)
menu_file.addAction(action_open)            # 執行對應函式

action_close = QtGui.QAction('Close')
# action_close = QtWidgets.QAction('OClose') # PyQt5 寫法
action_close.triggered.connect(close)
menu_file.addAction(action_close)            # 執行關閉應用程式函式

menubar.addMenu(menu_file)

Form.show()
sys.exit(app.exec())

