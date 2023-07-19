# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(300, 280)

label = QtWidgets.QLabel(MainWindow)  # 建立 QLabel
label.setGeometry(30, 10, 240, 40)    # 定義位置
# 定義樣式
label.setStyleSheet('''
    background:#ffffff;
    border:1px solid #000;
    font-size:20px;
    padding:5px;
''')
label.setAlignment(Qt.AlignmentFlag.AlignRight)    # 靠右對齊
label.setText('0')

# 定義按鈕群組中需要共用的變數
x = 30
y = 60
w = 60
h = 50

# 定義按鈕群組
btns = {
    '7':{'x':x,'y':y},
    '8':{'x':x+w,'y':y},
    '9':{'x':x+2*w,'y':y},
    '+':{'x':x+3*w,'y':y},
    '4':{'x':x,'y':y+h},
    '5':{'x':x+w,'y':y+h},
    '6':{'x':x+2*w,'y':y+h},
    '-':{'x':x+3*w,'y':y+h},
    '1':{'x':x,'y':y+2*h},
    '2':{'x':x+w,'y':y+2*h},
    '3':{'x':x+2*w,'y':y+2*h},
    '*':{'x':x+3*w,'y':y+2*h},
    'AC':{'x':x,'y':y+3*h},
    '0':{'x':x+w,'y':y+3*h},
    '=':{'x':x+2*w,'y':y+3*h},
    '/':{'x':x+3*w,'y':y+3*h},
}
# 依序取出按鈕群組中的每個項目
for i in btns:
    btns[i]['qw'] = QtWidgets.QPushButton(MainWindow) # 建立 QPuahButton
    # 定義樣式
    btns[i]['qw'].setStyleSheet('''
        QPushButton{
            font-size:16px;
            border-radius:5px;
            border:1px solid #000;
            background:#ccc;
            margin:3px;
        }
        QPushButton:pressed{
            background:#aaa;
        }
    ''')
    btns[i]['qw'].setText(i)   # 設定文字
    btns[i]['qw'].setGeometry(btns[i]['x'], btns[i]['y'], w, h)     # 設定位置和尺寸
    btns[i]['qw'].clicked.connect(lambda checked, n=i: showNum(n))  # 設定點擊按鈕時執行 showNum 函式

MainWindow.show()
sys.exit(app.exec())

