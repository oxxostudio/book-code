# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

listwidget = QtWidgets.QListWidget(Form)  # 建立列表選擇框元件
listwidget.addItems(['A','B','C','D'])    # 建立選單
listwidget.setGeometry(10,10,120,100)     # 設定位置

Form.show()
sys.exit(app.exec())

