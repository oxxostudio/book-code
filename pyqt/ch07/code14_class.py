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
        mbox.setText('hello?')   # 通知文字
        mbox.addButton(QtWidgets.QMessageBox.StandardButton.Ok)
        mbox.addButton(QtWidgets.QMessageBox.StandardButton.Open)
        mbox.addButton(QtWidgets.QMessageBox.StandardButton.Save)
        mbox.addButton(QtWidgets.QMessageBox.StandardButton.Cancel)
        # mbox.addButton(QtWidgets.QMessageBox.Ok)      # PyQt5 寫法
        # mbox.addButton(QtWidgets.QMessageBox.Open)    # PyQt5 寫法
        # mbox.addButton(QtWidgets.QMessageBox.Save)    # PyQt5 寫法
        # mbox.addButton(QtWidgets.QMessageBox.Cancel)  # PyQt5 寫法
        mbox.exec()             # 執行

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

