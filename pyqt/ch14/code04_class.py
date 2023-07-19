# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore
import sys
import datetime

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.GMT = datetime.timezone(datetime.timedelta(hours=8))

        self.label1 = QtWidgets.QLabel(self)          # 加入 QLabel 顯示文字
        self.label1.setGeometry(20,10,100,40)
        self.label1.setStyleSheet('font-size:20px;')
        self.label1.setText('目前時間：')

        self.label2 = QtWidgets.QLabel(self)          # 加入 QLabel 顯示時間
        self.label2.setGeometry(130,10,200,40)
        self.label2.setStyleSheet('font-size:20px;')

    def clock(self):
        now = datetime.datetime.now(tz=self.GMT).strftime('%H:%M:%S')   # 取得目前的時間，格式使用 H:M:S
        self.label2.setText(now)        # QLabel 顯示數字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    timer = QtCore.QTimer()             # 加入定時器
    timer.timeout.connect(Form.clock)   # 設定定時要執行的 function
    timer.start(1000)                   # 啟用定時器，設定間隔時間為 500 毫秒
    sys.exit(app.exec())

