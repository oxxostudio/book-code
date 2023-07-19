# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

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

bar = QtWidgets.QProgressBar(Form) # 進度條
bar.move(20,20)
bar.setRange(0, 200)      # 進度條範圍
bar.setValue(0)           # 進度條初始值
bar.setStyleSheet(style)  # 進度條樣式

n = 0
def more():
    global n
    n = n + 10
    bar.setValue(n)      # 增加進度

def reset():
    global n
    n = 0
    bar.reset()          # 重設進度

btn1 = QtWidgets.QPushButton(Form)   # 增加進度按鈕
btn1.move(20,60)
btn1.setText('增加進度')
btn1.clicked.connect(more)           # 點擊按鈕時執行函式

btn2 = QtWidgets.QPushButton(Form)   # 重設進度按鈕
btn2.move(110,60)
btn2.setText('重設')
btn2.clicked.connect(reset)          # 點擊按鈕時執行函式

Form.show()
sys.exit(app.exec())

