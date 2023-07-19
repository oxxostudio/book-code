# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setMouseTracking(True)
        self.setFocus()  # 設定為焦點
    # 關閉視窗
    def closeEvent(self, event):
        print('close!!')
    # 移動視窗
    def moveEvent(self, event):
        print('move...')
    # 視窗改變大小
    def resizeEvent(self, event):
        print('resize')
    # 顯示視窗
    def showEvent(self, event):
        print('show')
    # 成為焦點
    def focusInEvent(self, event):
        print('focus in')
    # 離開焦點
    def focusOutEvent(self, event):
        print('focus out')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

