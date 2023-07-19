# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

label = QtWidgets.QLabel(Form)
label.setText('hello world, how are you?')
label.setGeometry(30, 30, 100, 100)

label.setContentsMargins(0,0,0,0)          # 設定邊界
label.setWordWrap(True)                    # 可以換行
label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 對齊方式

font = QtGui.QFont()                       # 建立文字樣式元件
font.setFamily('Verdana')                  # 設定字體
font.setPointSize(20)                      # 文字大小
font.setBold(True)                         # 粗體
font.setItalic(True)                       # 斜體
font.setStrikeOut(True)                    # 刪除線
font.setUnderline(True)                    # 底線
label.setFont(font)                        # 設定文字樣式

Form.show()
sys.exit(app.exec())
