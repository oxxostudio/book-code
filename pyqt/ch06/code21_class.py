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
        self.n = 0

        self.bar = QtWidgets.QProgressBar(self)   # 進度條
        self.bar.move(20,20)
        self.bar.setRange(0, 200)                 # 進度條範圍
        self.bar.setValue(0)                      # 進度條初始值
        self.bar.setStyleSheet(style)             # 進度條樣式

        self.btn1 = QtWidgets.QPushButton(self)   # 增加進度按鈕
        self.btn1.move(20,60)
        self.btn1.setText('增加進度')
        self.btn1.clicked.connect(self.more)      # 點擊按鈕時執行函式

        self.btn2 = QtWidgets.QPushButton(self)   # 重設進度按鈕
        self.btn2.move(110,60)
        self.btn2.setText('重設')
        self.btn2.clicked.connect(self.reset)     # 點擊按鈕時執行函式

    def more(self):
        self.n = self.n + 10
        self.bar.setValue(self.n)      # 增加進度

    def reset(self):
        self.n = 0
        self.bar.reset()          # 重設進度

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

