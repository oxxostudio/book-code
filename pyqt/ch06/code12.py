# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

slider = QtWidgets.QSlider(Form)   # 加入數值調整滑桿
slider.move(20,20)

Form.show()
sys.exit(app.exec())

