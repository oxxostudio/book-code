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

label = QtWidgets.QLabel(MainWindow)
label.setGeometry(30, 10, 240, 40)
label.setStyleSheet('''
    background:#ffffff;
    border:1px solid #000;
    font-size:20px;
    padding:5px;
''')
label.setAlignment(Qt.AlignmentFlag.AlignRight)
label.setText('0')

num = '0'
def showNum(n):
    global num
    if n == 'AC':
        num = '0'
    elif n == '=':
        try:
            num = str(eval(num))
        except:
            num = 'error'
    else:
        if num == '0' and n in '0123456789':
            num = n
        else:
            num = num + n
    label.setText(num)
    if num == 'error':
        num = '0'

x = 30
y = 60
w = 60
h = 50
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

for i in btns:
    btns[i]['qw'] = QtWidgets.QPushButton(MainWindow)
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
    btns[i]['qw'].setText(i)
    btns[i]['qw'].setGeometry(btns[i]['x'], btns[i]['y'], w, h)
    btns[i]['qw'].clicked.connect(lambda checked, n=i: showNum(n))

MainWindow.show()
sys.exit(app.exec())

