# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)
screen =  QtWidgets.QApplication.screens()
# screen = QtWidgets.QApplication.desktop()   # PyQt5 寫法
screen_size = screen[0].size()
screen_w = screen_size.width()       # 電腦螢幕寬度
screen_h = screen_size.height()      # 電腦螢幕高度

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)
Form_w = Form.width()                # 視窗寬度
Form_h = Form.height()               # 視窗高度

new_x = int((screen_w - Form_w)/2)   # 計算後的 x 座標
new_y = int((screen_h - Form_h)/2)   # 計算後的 y 座標
Form.move(new_x, new_y)              # 移動視窗

Form.show()
sys.exit(app.exec())

