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

event = threading.Event()    # 建立事件

def a():
    event.wait()             # 等待事件被觸發
    for i in range(0,5):
        label_a.setText(str(i))
        print('A:',i)
        time.sleep(0.5)

def b():
    for i in range(0,50,10):
        if i>20:
            event.set()      # 觸發事件
        label_b.setText(str(i))
        print('B:',i)
        time.sleep(0.5)

thread_a = QThread()
thread_a.run = a
thread_a.start()

thread_b = QThread()
thread_b.run = b
thread_b.start()

Form.show()
print('主視窗出現')
sys.exit(app.exec())

