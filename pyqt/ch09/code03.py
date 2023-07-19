# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys, time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)      # 第一個 QLabel
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)      # 第二個 QLabel
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(0,5):
        label_a.setText(str(i))      # 每次迴圈執行時設定文字
        print('A:',i)
        time.sleep(0.5)              # 等待 0.5 秒

def b():
    for i in range(0,50,10):
        label_b.setText(str(i))      # 每次迴圈執行時設定文字
        print('B:',i)
        time.sleep(0.5)              # 等待 0.5 秒

a()          # 執行 a()
b()          # 執行 a()

Form.show()  # 顯示主視窗
print('主視窗出現')
sys.exit(app.exec())

