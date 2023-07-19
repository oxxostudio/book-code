# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets        # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6.QtCore import QThread   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys, time

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()
        self.run()

    def ui(self):
        self.label_a = QtWidgets.QLabel(self)      # 第一個 QLabel
        self.label_a.setGeometry(10, 10, 100, 30)

        self.label_b = QtWidgets.QLabel(self)      # 第二個 QLabel
        self.label_b.setGeometry(10, 50, 100, 30)

    def a(self):
        for i in range(0,5):
            self.label_a.setText(str(i))      # 每次迴圈執行時設定文字
            print('A:',i)
            time.sleep(0.5)              # 等待 0.5 秒

    def b(self):
        for i in range(0,50,10):
            self.label_b.setText(str(i))      # 每次迴圈執行時設定文字
            print('B:',i)
            time.sleep(0.5)              # 等待 0.5 秒

    def run(self):
        self.thread_a = QThread()
        self.thread_a.run = self.a
        self.thread_a.start()

        self.thread_b = QThread()
        self.thread_b.run = self.b
        self.thread_b.start()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    print('主視窗出現')
    sys.exit(app.exec())

