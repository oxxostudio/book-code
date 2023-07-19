# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets  # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def close(self):
    print('close!!')

def move(self):
    print('move...')

def resize(self):
    print('resize')

def show(self):
    print('show')

def focusIn(self):
    print('focus in')

def focusOut(self):
    print('focus out')

Form.closeEvent = close        # 關閉視窗
Form.moveEvent = move          # 移動視窗
Form.resizeEvent = resize      # 視窗改變大小
Form.showEvent = show          # 顯示視窗
Form.setFocus()                # 設定為焦點
Form.focusInEvent = focusIn    # 成為焦點
Form.focusOutEvent = focusOut  # 離開焦點

Form.show()
sys.exit(app.exec())

