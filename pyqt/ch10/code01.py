# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def mousePress(self):
    print('press')

Form.mousePressEvent  = mousePress    # 新增按下滑鼠事件，事件發生時執行 mousePress 函式

Form.show()
sys.exit(app.exec())

