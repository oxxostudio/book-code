# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(['A','B','C','D'])
listwidget.setGeometry(10,10,120,100)
item = listwidget.takeItem(1)       # 取得第二個項目，也就是 B
listwidget.removeItemWidget(item)   # 移除第二個項目

Form.show()
sys.exit(app.exec())

