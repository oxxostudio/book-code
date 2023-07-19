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

bar1 = QtWidgets.QProgressBar(Form)  # 第一種格式進度條
bar1.move(20,20)
bar1.setRange(0, 200)
bar1.setValue(50)
bar1.setStyleSheet(style)
bar1.setFormat('%v/%m')

bar2 = QtWidgets.QProgressBar(Form)  # 第二種格式進度條
bar2.move(20,60)
bar2.setRange(0, 200)
bar2.setValue(50)
bar2.setStyleSheet(style)
bar2.setFormat('%p%')

bar3 = QtWidgets.QProgressBar(Form)  # 第三種格式進度條
bar3.move(20,100)
bar3.setRange(0, 200)
bar3.setValue(50)
bar3.setStyleSheet(style)
bar3.setFormat('%v')

Form.show()
sys.exit(app.exec())

