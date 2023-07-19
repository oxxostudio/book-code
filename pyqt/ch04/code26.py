# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

arr = ['']*3                  # 先新增一個串列放入文字
def show(cb, i):
    global a
    if cb.isChecked():
        arr[i] = cb.text()    # 如果該按鈕是勾選狀態，在串列的指定位置放入文字
    else:
        arr[i] = ''           # 如果該按鈕是勾選狀態，在串列的指定位置放入空字串
    output = ''.join(arr)     # 組合串列內容為文字
    label.setText(output)     # label 顯示文字

label = QtWidgets.QLabel(Form)
label.setGeometry(30, 30, 100, 30)

cb_a = QtWidgets.QCheckBox(Form)
cb_a.move(30, 60)
cb_a.setText('A')
cb_a.clicked.connect(lambda:show(cb_a, 0))  # 點擊按鈕時，回傳兩個參數給 show 函式

cb_b = QtWidgets.QCheckBox(Form)
cb_b.move(80, 60)
cb_b.setText('B')
cb_b.clicked.connect(lambda:show(cb_b, 1))  # 點擊按鈕時，回傳兩個參數給 show 函式

cb_c = QtWidgets.QCheckBox(Form)
cb_c.move(130, 60)
cb_c.setText('C')
cb_c.clicked.connect(lambda:show(cb_c, 2))  # 點擊按鈕時，回傳兩個參數給 show 函式

Form.show()
sys.exit(app.exec())
