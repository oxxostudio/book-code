# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.listwidget = QtWidgets.QListWidget(self)
        self.listwidget.addItems(['A','B','C','D'])
        self.listwidget.setGeometry(10,10,120,120)
        self.listwidget.addItem('X')                         # 添加純文字項目
        self.listwidget.addItem(self.create_item('', 'icon.png')) # 添加使用函式創造的選項

        self.listwidget.insertItem(0, 'Y')                          # 添加純文字項目
        self.listwidget.insertItem(0, self.create_item('', 'mona.jpg'))  # 添加使用函式創造的選項

    def create_item(self, text, img):
        item = QtWidgets.QListWidgetItem()      # 建立清單項目
        item.setText(text)                      # 項目文字
        item.setIcon(QtGui.QIcon(img))          # 項目圖片
        return item                             # 返回清單項目

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

