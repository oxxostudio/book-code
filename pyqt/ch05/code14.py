# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets, QtGui     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def create_item(text):
    item = QtWidgets.QListWidgetItem(listwidget)
    item.setText(text)
    item.setIcon(QtGui.QIcon('icon.png'))
    return item

listwidget = QtWidgets.QListWidget(Form)
listwidget.addItems(['A','B','C','D'])
listwidget.setGeometry(10,10,200,50)
listwidget.addItem(create_item(''))
listwidget.setFlow(QtWidgets.QListView.Flow.LeftToRight)  # PyQt6 寫法，改成水平顯示
# listwidget.setFlow(QtWidgets.QListView.LeftToRight)     # 這行是 PyQt5 的寫法
listwidget.setStyleSheet('''
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

Form.show()
sys.exit(app.exec())

