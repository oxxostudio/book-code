# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

now = QtCore.QTime.currentTime()

t1 = QtWidgets.QTimeEdit(Form)
t1.setGeometry(20,20,120,30)
t1.setDisplayFormat('hh:mm:ss')   # 24 小時制
t1.setTime(now)

t2 = QtWidgets.QTimeEdit(Form)
t2.setGeometry(20,60,120,30)
t2.setDisplayFormat('hh:mm ap')   # 上午下午制，上午下午在後面
t2.setTime(now)

t3 = QtWidgets.QTimeEdit(Form)
t3.setGeometry(20,100,120,30)
t3.setDisplayFormat('ap hh:mm:ss')  # 上午下午制，上午下午在前面
t3.setTime(now)

Form.show()
sys.exit(app.exec())

