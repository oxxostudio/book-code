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
        self.arr = ['']*3                  # 先新增一個串列放入文字

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30, 30, 100, 30)

        self.cb_a = QtWidgets.QCheckBox(self)
        self.cb_a.move(30, 60)
        self.cb_a.setText('A')
        self.cb_a.clicked.connect(lambda:self.showText(self.cb_a, 0))  # 點擊按鈕時，回傳兩個參數給 show 函式

        self.cb_b = QtWidgets.QCheckBox(self)
        self.cb_b.move(80, 60)
        self.cb_b.setText('B')
        self.cb_b.clicked.connect(lambda:self.showText(self.cb_b, 1))  # 點擊按鈕時，回傳兩個參數給 show 函式

        self.cb_c = QtWidgets.QCheckBox(self)
        self.cb_c.move(130, 60)
        self.cb_c.setText('C')
        self.cb_c.clicked.connect(lambda:self.showText(self.cb_c, 2))  # 點擊按鈕時，回傳兩個參數給 show 函式

    def showText(self, cb, i):
        if cb.isChecked():
            self.arr[i] = cb.text()    # 如果該按鈕是勾選狀態，在串列的指定位置放入文字
        else:
            self.arr[i] = ''           # 如果該按鈕是勾選狀態，在串列的指定位置放入空字串
        output = ''.join(self.arr)     # 組合串列內容為文字
        self.label.setText(output)     # label 顯示文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
