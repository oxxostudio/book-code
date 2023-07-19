# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setMouseTracking(True)
        self.screen()
        self.windowMove()

    def screen(self):
        screen =  QtWidgets.QApplication.screens()
        # screen = QtWidgets.QApplication.desktop()    # PyQt5 寫法
        screen_size = screen[0].size()
        self.screen_w = screen_size.width()            # 電腦螢幕寬度
        self.screen_h = screen_size.height()           # 電腦螢幕高度

    def windowMove(self):
        Form_w = self.width()                          # 視窗寬度
        Form_h = self.height()                         # 視窗高度
        new_x = int((self.screen_w - Form_w)/2)        # 計算後的 x 座標
        new_y = int((self.screen_h - Form_h)/2)        # 計算後的 y 座標
        self.move(new_x, new_y)                        # 移動視窗

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

