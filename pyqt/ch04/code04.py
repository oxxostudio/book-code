# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(320, 240)

label = QtWidgets.QLabel(Form)
label.setGeometry(20, 20, 200, 150)

img = QtGui.QImage('mona.jpg')                 # 讀取圖片
label.setPixmap(QtGui.QPixmap.fromImage(img))  # 加入圖片

Form.show()
sys.exit(app.exec())
