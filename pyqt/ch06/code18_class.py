# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.bar1 = QtWidgets.QProgressBar(self)
        self.bar1.move(20,20)
        self.bar1.setRange(0, 100)
        self.bar1.setValue(50)
        self.bar1.setStyleSheet('''
            QProgressBar {
                border: 2px solid #000;
                border-radius: 5px;
                text-align:center;
                height: 50px;
                width:80px;
            }
            QProgressBar::chunk {
                background: #09c;
                width:1px;
            }
        ''')

        self.bar2 = QtWidgets.QProgressBar(self)
        self.bar2.move(120,20)
        self.bar2.setRange(0, 100)
        self.bar2.setValue(50)
        self.bar2.setStyleSheet('''
            QProgressBar {
                border: 2px solid #000;
                text-align:center;
                background:#aaa;
                color:#fff;
                height: 15px;
                border-radius: 8px;
                width:150px;
            }
            QProgressBar::chunk {
                background: #333;
                width:1px;
            }
        ''')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

