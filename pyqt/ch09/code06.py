# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets        # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtCore import QThread   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys, time, threading

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label_a = QtWidgets.QLabel(Form)
label_a.setGeometry(10, 10, 100, 30)

label_b = QtWidgets.QLabel(Form)
label_b.setGeometry(10, 50, 100, 30)

def a():
    for i in range(1,6):
        label_a.setText(str(i))
        print('A:',i)
        time.sleep(0.5)

def b():
    for i in range(10,60,10):
        label_b.setText(str(i))
        print('B:',i)
        time.sleep(0.5)

thread_a = threading.Thread(target=a)   # 建立執行緒，執行 a 函式
thread_b = threading.Thread(target=b)   # 建立執行緒，執行 b 函式

thread_a.start()   # 啟動執行緒
thread_b.start()   # 啟動執行緒

Form.show()
print('主視窗出現')
sys.exit(app.exec())
