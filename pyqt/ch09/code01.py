# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)          # 加入 QLabel 顯示數字
label.setGeometry(20,10,100,40)
label.setStyleSheet('font-size:30px;')

a = 0
def count():
    global a
    a = a + 1                  # 數字增加 1
    label.setText(str(a))      # QLabel 顯示數字

timer = QtCore.QTimer()        # 加入定時器
timer.timeout.connect(count)   # 設定定時要執行的 function
timer.start(500)               # 啟用定時器，設定間隔時間為 500 毫秒

Form.show()
sys.exit(app.exec())

