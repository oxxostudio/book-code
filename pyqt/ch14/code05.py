# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore
import sys
import datetime

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

# 定義產生不同時區時間的函式
GMT = datetime.timezone(datetime.timedelta(hours=8))
def timezone(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h))      # 取得時區
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')  # 取得該時區的時間
    return now

name = ['倫敦','台灣','日本','紐約']          # 四個時區的名稱串列
loc_time = [1,8,9,-4]                      # 四個時區的 GMT 數字
labels_1 = {}
labels_2 = {}

for i in name:
    index = name.index(i)                               # 位置對應順序
    labels_1[i] = QtWidgets.QLabel(Form)                # 加入 QLabel 顯示位置
    labels_1[i].setGeometry(20, 10+index*30, 100, 40)
    labels_1[i].setStyleSheet('font-size:20px;')
    labels_1[i].setText(f'{i}時間：')
    labels_2[i] = QtWidgets.QLabel(Form)                # 加入 QLabel 顯示時間
    labels_2[i].setGeometry(130, 10+index*30, 100, 40)
    labels_2[i].setStyleSheet('font-size:20px;')
    labels_2[i].setText(f'{timezone(loc_time[index])}') # 取得該時區的時間

def clock():
    for i in name:
        index = name.index(i)
        labels_2[i].setText(f'{timezone(loc_time[index])}')

timer = QtCore.QTimer()        # 加入定時器
timer.timeout.connect(clock)   # 設定定時要執行的 function
timer.start(1000)              # 啟用定時器，設定間隔時間為 500 毫秒

Form.show()
sys.exit(app.exec())


