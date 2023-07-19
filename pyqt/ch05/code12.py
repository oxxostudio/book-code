# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def create_item(text, img):
    item = QtWidgets.QListWidgetItem()      # 建立清單項目
    item.setText(text)                      # 項目文字
    item.setIcon(QtGui.QIcon(img))          # 項目圖片
    return item                             # 返回清單項目

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(['A','B','C','D'])
listwidget.setGeometry(10,10,120,120)
listwidget.addItem('X')                         # 添加純文字項目
listwidget.addItem(create_item('', 'icon.png')) # 添加使用函式創造的選項

listwidget.insertItem(0, 'Y')                          # 添加純文字項目
listwidget.insertItem(0, create_item('', 'mona.jpg'))  # 添加使用函式創造的選項

Form.show()
sys.exit(app.exec())

