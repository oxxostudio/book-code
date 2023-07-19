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
        self.name = ['倫敦','台灣','日本','紐約']          # 四個時區的名稱串列
        self.loc_time = [1,8,9,-4]                      # 四個時區的 GMT 數字
        self.labels_1 = {}
        self.labels_2 = {}

        for i in self.name:
            index = self.name.index(i)                               # 位置對應順序
            self.labels_1[i] = QtWidgets.QLabel(self)                # 加入 QLabel 顯示位置
            self.labels_1[i].setGeometry(20, 10+index*30, 100, 40)
            self.labels_1[i].setStyleSheet('font-size:20px;')
            self.labels_1[i].setText(f'{i}時間：')
            self.labels_2[i] = QtWidgets.QLabel(self)                # 加入 QLabel 顯示時間
            self.labels_2[i].setGeometry(130, 10+index*30, 100, 40)
            self.labels_2[i].setStyleSheet('font-size:20px;')
            self.labels_2[i].setText(f'{self.timezone(self.loc_time[index])}') # 取得該時區的時間

    def timezone(self, h):
        GMT = datetime.timezone(datetime.timedelta(hours=h))      # 取得時區
        now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')  # 取得該時區的時間
        return now

    def clock(self):
        for i in self.name:
            index = self.name.index(i)
            self.labels_2[i].setText(f'{self.timezone(self.loc_time[index])}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    timer = QtCore.QTimer()        # 加入定時器
    timer.timeout.connect(Form.clock)   # 設定定時要執行的 function
    timer.start(1000)              # 啟用定時器，設定間隔時間為 500 毫秒
    sys.exit(app.exec())

