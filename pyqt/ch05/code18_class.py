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
        self.box = QtWidgets.QComboBox(self)
        self.box.addItems(['A','B','C','D'])
        self.box.setGeometry(10,10,200,30)

        self.box.addItem('apple')     # 在最後方添加 apple 選項
        self.box.removeItem(2)        # 移除第三個選項 C
        self.box.insertItem(0, 'ok')  # 在最前方加入 ok 為第一個選項

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

