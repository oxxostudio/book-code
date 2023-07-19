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
        mbox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No | QtWidgets.QMessageBox.StandardButton.Cancel)
        mbox.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        ret = mbox.exec()  # 取得點擊的按鈕數字
        if ret == QtWidgets.QMessageBox.StandardButton.Yes:
            print(1)
        elif ret == QtWidgets.QMessageBox.StandardButton.No:
            print(2)
        elif ret == QtWidgets.QMessageBox.StandardButton.Cancel:
            print(3)           # 執行
        # 下方為 PyQt5 寫法
        # mbox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        # mbox.setDefaultButton(QtWidgets.QMessageBox.Yes)
        # ret = mbox.exec()                      # 取得點擊的按鈕數字
        # if ret == QtWidgets.QMessageBox.Yes:
        #     print(1)
        # elif ret == QtWidgets.QMessageBox.No:
        #     print(2)
        # elif ret == QtWidgets.QMessageBox.Cancel:
        #     print(3)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

