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
        style = '''
            QProgressBar {
                border: 2px solid #000;
                border-radius: 5px;
                text-align:center;
                height: 20px;
                width:200px;
            }
            QProgressBar::chunk {
                background: #09c;
                width:1px;
            }
        '''

        self.bar1 = QtWidgets.QProgressBar(self)
        self.bar1.move(20,20)
        self.bar1.setRange(0, 200)
        self.bar1.setValue(50)
        self.bar1.setStyleSheet(style)
        self.bar1.setFormat('%v/%m')  # 第一種格式進度條

        self.bar2 = QtWidgets.QProgressBar(self)
        self.bar2.move(20,60)
        self.bar2.setRange(0, 200)
        self.bar2.setValue(50)
        self.bar2.setStyleSheet(style)
        self.bar2.setFormat('%p%')  # 第三種格式進度條

        self.bar3 = QtWidgets.QProgressBar(self)
        self.bar3.move(20,100)
        self.bar3.setRange(0, 200)
        self.bar3.setValue(50)
        self.bar3.setStyleSheet(style)
        self.bar3.setFormat('%v')  # 第三種格式進度條

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
