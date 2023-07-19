# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,20,100,30)

def show():
    label.setText(str(slider.value()))  # 顯示滑桿數值

slider = QtWidgets.QSlider(Form)
slider.setGeometry(20,40,100,30)
slider.setRange(0, 100)
slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
# slider.setOrientation(1)           # PyQt5 寫法
slider.valueChanged.connect(show)    # 數值改變時連動對應函式
Form.show()
sys.exit(app.exec())

