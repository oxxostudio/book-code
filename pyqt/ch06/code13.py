# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

slider_1 = QtWidgets.QSlider(Form)   # 預設垂直
slider_1.move(20,20)

slider_2 = QtWidgets.QSlider(Form)
slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal) # 設定為水平
# slider_2.setOrientation(1)    # 這行是 PyQt5 寫法：設定為水平
slider_2.move(50,20)

Form.show()
sys.exit(app.exec())

