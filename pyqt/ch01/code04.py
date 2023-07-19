# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')  # 設定視窗標題
        self.resize(300, 200)               # 設定視窗尺寸
        self.setUpdatesEnabled(True)
        self.ui()                           # 執行 ui() 方法

    def ui(self):
        self.label = QtWidgets.QLabel(self) # 在 Form 裡加入標籤
        self.label.setText('hello world')   # 設定標籤文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()                       # 建立視窗元件
    Form.show()                             # 顯示視窗
    sys.exit(app.exec())
