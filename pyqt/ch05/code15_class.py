# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(10,10,120,30)
        self.listwidget = QtWidgets.QListWidget(self)
        self.listwidget.addItems(['A','B','C','D'])
        self.listwidget.setGeometry(10,50,120,50)
        self.listwidget.setFlow(QtWidgets.QListView.Flow.LeftToRight)  # 這行是 PyQt6 的寫法

        # self.listwidget.setFlow(QtWidgets.QListView.LeftToRight)     # 這行是 PyQt5 的寫法
        self.listwidget.setStyleSheet('''
            QListWidget::item{
                font-size:20px;
            }
            QListWidget::item:selected{
                color:#f00;
                background:#000;
            }
        ''')
        self.listwidget.clicked.connect(self.showText)  # 點擊項目時執行函式

    def showText(self):
        text = self.listwidget.currentItem().text()  # 取得項目文字
        num = self.listwidget.currentIndex().row()   # 取得項目編號
        self.label.setText(f'{num}:{text}')          # 顯示文字

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

