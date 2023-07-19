# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('hello world, how are you?')
        self.label.setGeometry(30, 30, 100, 100)

        self.label.setContentsMargins(0,0,0,0)     # 設定邊界
        self.label.setWordWrap(True)               # 可以換行
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 對齊方式

        font = QtGui.QFont()                       # 建立文字樣式元件
        font.setFamily('Verdana')                  # 設定字體
        font.setPointSize(20)                      # 文字大小
        font.setBold(True)                         # 粗體
        font.setItalic(True)                       # 斜體
        font.setStrikeOut(True)                    # 刪除線
        font.setUnderline(True)                    # 底線
        self.label.setFont(font)                   # 設定文字樣式

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
