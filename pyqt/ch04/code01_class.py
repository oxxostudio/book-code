# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.ui()                             # 執行元件裡的 ui() 方法

    def ui(self):
        self.label = QtWidgets.QLabel(self)   # 在 Form 裡加入標籤
        self.label.setText('hello world')     # 設定標籤文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()        # 建立視窗元件
    Form.show()              # 顯示視窗
    sys.exit(app.exec())
