# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore, QtWebEngineWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(800, 600)

widget = QtWebEngineWidgets.QWebEngineView(Form)  # 建立網頁顯示元件
widget.move(0,0)
widget.resize(800, 600)
widget.load(QtCore.QUrl("https://google.com"))    # 載入網頁

Form.show()
sys.exit(app.exec())

