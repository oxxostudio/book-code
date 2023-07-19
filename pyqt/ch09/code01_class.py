# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)          # 加入 QLabel 顯示數字
        self.label.setGeometry(20,10,100,40)
        self.label.setStyleSheet('font-size:30px;')

        self.a = 0

        self.timer = QtCore.QTimer()             # 加入定時器
        self.timer.timeout.connect(self.count)   # 設定定時要執行的 function
        self.timer.start(500)                    # 啟用定時器，設定間隔時間為 500 毫秒

    def count(self):
        self.a = self.a + 1                  # 數字增加 1
        self.label.setText(str(self.a))      # QLabel 顯示數字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

