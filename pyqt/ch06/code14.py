# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

slider_1 = QtWidgets.QSlider(Form)
slider_1.move(20,20)
slider_1.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_1.setTickPosition(slider_1.TickPosition.TicksAbove) # 下方加入刻度線
# slider_1.setOrientation(1)   # PyQt5 寫法
# slider_1.setTickPosition(2)  # PyQt5 寫法
slider_1.setTickInterval(10)   # 刻度線間距 ( 會有十條刻度線 )

slider_2 = QtWidgets.QSlider(Form)
slider_2.move(20,60)
slider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
slider_2.setTickPosition(slider_1.TickPosition.TicksBothSides) # 上下都加入刻度線
# slider_2.setOrientation(1)   # PyQt5 寫法
# slider_2.setTickPosition(3)  # PyQt5 寫法
slider_2.setTickInterval(20)   # 刻度線間距 ( 會有五條刻度線 )

Form.show()
sys.exit(app.exec())

