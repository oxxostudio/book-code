# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(20,20,120,30)

def show():
    label.setText(t1.time().toString())  # 顯示時間

now = QtCore.QTime.currentTime()   # 取得目前電腦時間

t1 = QtWidgets.QTimeEdit(Form)
t1.setGeometry(140,20,120,30)
t1.setDisplayFormat('hh:mm:ss')
t1.setTime(now)                    # 設定時間
t1.setTimeRange(QtCore.QTime(3, 00, 00), QtCore.QTime(23, 30, 00))
t1.timeChanged.connect(show)

Form.show()
sys.exit(app.exec())

