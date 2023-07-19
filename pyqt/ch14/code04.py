# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets, QtCore
import sys
import datetime

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

label1 = QtWidgets.QLabel(Form)          # 加入 QLabel 顯示文字
label1.setGeometry(20,10,100,40)
label1.setStyleSheet('font-size:20px;')
label1.setText('目前時間：')

label2 = QtWidgets.QLabel(Form)          # 加入 QLabel 顯示時間
label2.setGeometry(130,10,200,40)
label2.setStyleSheet('font-size:20px;')

GMT = datetime.timezone(datetime.timedelta(hours=8))
def count():
    now = datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')   # 取得目前的時間，格式使用 H:M:S
    label2.setText(now)        # QLabel 顯示數字

timer = QtCore.QTimer()        # 加入定時器
timer.timeout.connect(count)   # 設定定時要執行的 function
timer.start(1000)              # 啟用定時器，設定間隔時間為 500 毫秒

Form.show()
sys.exit(app.exec())

