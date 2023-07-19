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
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText('open')
        self.btn.clicked.connect(self.showBox)

    def showBox(self):
        mbox = QtWidgets.QMessageBox(self)
        mbox.setText('hello')
        a = mbox.addButton('Apple',mbox.ButtonRole.ActionRole)   # 前方多了變數 a
        b = mbox.addButton('Banana',mbox.ButtonRole.ActionRole)  # 前方多了變數 b
        c = mbox.addButton('Orange',mbox.ButtonRole.ActionRole)  # 前方多了變數 c
        # a = mbox.addButton('Apple',3)   # PyQt5 寫法
        # b = mbox.addButton('Banana',3)  # PyQt5 寫法
        # c = mbox.addButton('Orange',3)  # PyQt5 寫法
        mbox.setDefaultButton(b)        # 預先選取 b
        mbox.exec()
        text = mbox.clickedButton().text()   # 取得點擊的按鈕文字
        if text == 'Apple':
            print('Apple')
        if text == 'Banana':
            print('Banana')
        if text == 'Orange':
            print('Orange')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

