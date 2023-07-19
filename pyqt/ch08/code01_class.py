# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        # 垂直 Layout
        self.vbox = QtWidgets.QWidget(self)         # 建立一個新的 Widget
        self.vbox.setGeometry(0,0,150,150)          # 設定 Widget 大小

        self.v_layout = QtWidgets.QVBoxLayout(self.vbox) # 建立垂直 Layout

        self.btn1 = QtWidgets.QPushButton(self)     # 在視窗中加入一個 QPushButton
        self.btn1.setText('1')                      # 按鈕文字
        self.v_layout.addWidget(self.btn1)          # 將按鈕放入 v_layout 中

        self.btn2 = QtWidgets.QPushButton(self)     # 在視窗中加入一個 QPushButton
        self.btn2.setText('2')                      # 按鈕文字
        self.v_layout.addWidget(self.btn2)          # 將按鈕放入 v_layout 中

        self.btn3 = QtWidgets.QPushButton(self)     # 在視窗中加入一個 QPushButton
        self.btn3.setText('3')                      # 按鈕文字
        self.v_layout.addWidget(self.btn3)          # 將按鈕放入 v_layout 中

        # 水平 Layout
        self.hbox = QtWidgets.QWidget(self)         # 建立一個新的 Widget
        self.hbox.setGeometry(150,0,150,150)        # 設定 Widget 大小

        self.h_layout = QtWidgets.QHBoxLayout(self.hbox) # 建立水平 Layout

        self.btn4 = QtWidgets.QPushButton(self)     # 在視窗中加入一個 QPushButton
        self.btn4.setText('4')                      # 按鈕文字
        self.h_layout.addWidget(self.btn4)          # 將按鈕放入 h_layout 中

        self.btn5 = QtWidgets.QPushButton(self)     # 在視窗中加入一個 QPushButton
        self.btn5.setText('5')                      # 按鈕文字
        self.h_layout.addWidget(self.btn5)          # 將按鈕放入 h_layout 中

        self.btn6 = QtWidgets.QPushButton(self)     # 在視窗中加入一個 QPushButton
        self.btn6.setText('6')                      # 按鈕文字
        self.h_layout.addWidget(self.btn6)          # 將按鈕放入 h_layout 中

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

