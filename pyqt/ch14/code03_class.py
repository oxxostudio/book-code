# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 280)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30, 10, 240, 40)
        self.label.setStyleSheet('''
            background:#ffffff;
            border:1px solid #000;
            font-size:20px;
            padding:5px;
        ''')
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label.setText('0')
        self.num = '0'

        x = 30
        y = 60
        w = 60
        h = 50
        self.btns = {
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

        for i in self.btns:
            self.btns[i]['qw'] = QtWidgets.QPushButton(self)
            self.btns[i]['qw'].setStyleSheet('''
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
            self.btns[i]['qw'].setText(i)
            self.btns[i]['qw'].setGeometry(self.btns[i]['x'], self.btns[i]['y'], w, h)
            self.btns[i]['qw'].clicked.connect(lambda checked, n=i: self.showNum(n))

    def showNum(self, n):
        if n == 'AC':
            self.num = '0'
        elif n == '=':
            try:
                self.num = str(eval(self.num))
            except:
                self.num = 'error'
        else:
            if self.num == '0' and n in '0123456789':
                self.num = n
            else:
                self.num = self.num + n
        self.label.setText(self.num)
        if self.num == 'error':
            self.num = '0'

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

