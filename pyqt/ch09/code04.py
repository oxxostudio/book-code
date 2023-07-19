# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets        # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtCore import QThread   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys, time

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(0,5):
        label_a.setText(str(i))
        print('A:',i)
        time.sleep(0.5)

def b():
    for i in range(0,50,10):
        label_b.setText(str(i))
        print('B:',i)
        time.sleep(0.5)

thread_a = QThread()   # 建立 Thread()
thread_a.run = a       # 設定該執行緒執行 a()
thread_a.start()       # 啟動執行緒

thread_b = QThread()   # 建立 Thread()
thread_b.run = b       # 設定該執行緒執行 b()
thread_b.start()       # 啟動執行緒

Form.show()
print('主視窗出現')
sys.exit(app.exec())

