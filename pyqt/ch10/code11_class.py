# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

# 主視窗
class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('測試文字')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('開啟新視窗')
        self.btn.setStyleSheet('font-size:16px;')
        self.btn.setGeometry(40,60,120,40)
        self.btn.clicked.connect(self.showNewWindow)

    def showNewWindow(self):
        self.nw = newWindow()       # 連接新視窗
        self.nw.show()              # 顯示新視窗
        x = self.nw.pos().x()       # 取得新視窗目前 x 座標
        y = self.nw.pos().y()       # 取得新視窗目前 y 座標
        self.nw.move(x+100, y+100)  # 移動新視窗位置

# 新視窗
class newWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio.2')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('test')
        self.btn.setStyleSheet('font-size:16px;')
        self.btn.setGeometry(40,60,120,40)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

