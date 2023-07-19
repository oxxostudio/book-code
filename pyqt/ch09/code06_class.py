# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets        # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtCore import QThread   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys, time, threading

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.event = threading.Event()
        self.ui()
        self.run()

    def ui(self):
        self.label_a = QtWidgets.QLabel(self)
        self.label_a.setGeometry(10, 10, 100, 30)

        self.label_b = QtWidgets.QLabel(self)
        self.label_b.setGeometry(10, 50, 100, 30)

    def a(self):
        self.event.wait()             # 等待事件被觸發
        for i in range(0,5):
            self.label_a.setText(str(i))
            print('A:',i)
            time.sleep(0.5)

    def b(self):
        for i in range(0,50,10):
            if i>20:
                self.event.set()      # 觸發事件
            self.label_b.setText(str(i))
            print('B:',i)
            time.sleep(0.5)

    def run(self):
        self.thread_a = threading.Thread(target=self.a)   # 建立執行緒，執行 a 函式
        self.thread_b = threading.Thread(target=self.b)   # 建立執行緒，執行 b 函式

        self.thread_a.start()   # 啟動執行緒
        self.thread_b.start()   # 啟動執行緒

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    print('主視窗出現')
    sys.exit(app.exec())

