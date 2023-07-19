# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.d1 = QtWidgets.QDateEdit(self)
        self.d1.setGeometry(20,20,100,30)
        self.d1.setDisplayFormat('dd/MM/yyyy')  # 設定格式 西元年/月/日

        self.d2 = QtWidgets.QDateEdit(self)
        self.d2.setGeometry(130,20,100,30)
        self.d2.setDisplayFormat('yyyy/MM/dd')  # 設定格式 日/月/西元年

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

