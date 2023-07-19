# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtCore, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,120,30)

def show():
    text = listwidget.currentItem().text()  # 取得項目文字
    num = listwidget.currentIndex().row()   # 取得項目編號
    label.setText(f'{num}:{text}')          # 顯示文字

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(['A','B','C','D'])
listwidget.setGeometry(10,50,120,50)
listwidget.setFlow(QtWidgets.QListView.Flow.LeftToRight)  # 這行是 PyQt6 的寫法

# listwidget.setFlow(QtWidgets.QListView.LeftToRight)     # 這行是 PyQt5 的寫法
listwidget.setStyleSheet('''
    QListWidget::item{
        font-size:20px;
    }
    QListWidget::item:selected{
        color:#f00;
        background:#000;
    }
''')
listwidget.clicked.connect(show)         # 點擊項目時執行函式

Form.show()
sys.exit(app.exec())

