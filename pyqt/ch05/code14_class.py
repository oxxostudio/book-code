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
        self.listwidget = QtWidgets.QListWidget(self)
        self.listwidget.addItems(['A','B','C','D'])
        self.listwidget.setGeometry(10,10,200,50)
        self.listwidget.addItem(self.create_item(''))
        self.listwidget.setFlow(QtWidgets.QListView.Flow.LeftToRight)  # PyQt6 寫法，改成水平顯示
        # self.listwidget.setFlow(QtWidgets.QListView.LeftToRight)     # 這行是 PyQt5 的寫法水平顯示
        self.listwidget.setStyleSheet('''
            QListWidget{
                color:#00f;
            }
            QListWidget::item{
                width:30px;
            }
            QListWidget::item:selected{
                color:#f00;
                background:#000;
            }
        ''')

    def create_item(self, text):
        item = QtWidgets.QListWidgetItem(self.listwidget)
        item.setText(text)
        item.setIcon(QtGui.QIcon('icon.png'))
        return item

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

