# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(['A','B','C','D'])
listwidget.setGeometry(10,10,120,100)
item = listwidget.item(1)                # 取得第二個項目 ( 第一個為 0 )
item.setText('ok')                       # 設定文字為 ok
item.setIcon(QtGui.QIcon('icon.png'))    # 設定 icon

Form.show()
sys.exit(app.exec())

