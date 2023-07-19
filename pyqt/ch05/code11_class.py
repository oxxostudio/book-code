# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
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
        self.listwidget.setGeometry(10,10,120,100)
        item = self.listwidget.takeItem(1)       # 取得第二個項目，也就是 B
        self.listwidget.removeItemWidget(item)   # 移除第二個項目

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

