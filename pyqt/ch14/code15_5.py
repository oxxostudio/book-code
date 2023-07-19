# Copyright © https://steam.oxxostudio.tw

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(400, 300)

canvas = QPixmap(400,240)
canvas.fill(QColor('#ffffff'))

label = QtWidgets.QLabel(MainWindow)
label.setGeometry(0, 0, 400, 240)
label.setPixmap(canvas)

last_x, last_y = None, None
penSize = 10
penColor = QColor('#000000')

def release(self):
    global last_x, last_y
    last_x, last_y = None, None

def mousePress(self):
    global penColor, penSize
    qpainter = QPainter()
    qpainter.begin(label.pixmap())
    qpainter.setPen(QPen(QColor(penColor), penSize, Qt.SolidLine, Qt.RoundCap))
    qpainter.drawPoint(self.x(), self.y())
    qpainter.end()
    MainWindow.update()

def draw(self):
    global last_x, last_y, penColor, penSize
    if last_x is None:
        last_x = self.x()
        last_y = self.y()
        return
    qpainter = QPainter()
    qpainter.begin(label.pixmap())
    qpainter.setPen(QPen(penColor, penSize, Qt.SolidLine, Qt.RoundCap))
    qpainter.drawLine(last_x, last_y, self.x(), self.y())
    qpainter.end()
    MainWindow.update()
    last_x = self.x()
    last_y = self.y()

label.mousePressEvent  = mousePress
label.mouseMoveEvent = draw
label.mouseReleaseEvent = release

def changeColor(self, color):
    global penColor, btn
    penColor = QColor(color)
    for i in btn:
        btn[i].setDisabled(False)
    self.setDisabled(True)

colors = ['#ff0000','#ff8800','#ffee00','#00cc00','#0066ff','#0000cc','#cc00cc','#000000','#ffffff']
btn = {}
for i in colors:
    index = colors.index(i)
    btn[i] = QtWidgets.QPushButton(MainWindow)
    btn[i].setStyleSheet('''
        QPushButton{
            background:'''+i+''';
            margin-right:5px;
        }
        QPushButton:disabled{
            border:3px solid #000;
        }
    ''')
    btn[i].setGeometry(index*30+10,250,30,30)
    btn[i].clicked.connect(lambda checked, b=btn[i], c=i:  changeColor(b, c))

def changeSize(self, size):
    global penSize
    btn_s.setDisabled(False)
    btn_m.setDisabled(False)
    btn_l.setDisabled(False)
    penSize = size
    self.setDisabled(True)

btn_s = QtWidgets.QPushButton(MainWindow)
btn_s.setText('細')
btn_s.setGeometry(280, 250, 45, 30)
btn_s.clicked.connect(lambda: changeSize(btn_s, 3))
btn_m = QtWidgets.QPushButton(MainWindow)
btn_m.setText('中')
btn_m.setGeometry(315, 250, 45, 30)
btn_m.setDisabled(True)
btn_m.clicked.connect(lambda: changeSize(btn_m, 10))
btn_l = QtWidgets.QPushButton(MainWindow)
btn_l.setText('粗')
btn_l.setGeometry(350, 250, 45, 30)
btn_l.clicked.connect(lambda: changeSize(btn_l, 20))

def newFile():
    ret = mbox.question(MainWindow, 'question', '確定開新檔案？')
    if ret == mbox.Yes:
        canvas.fill(QColor('#ffffff'))
        label.setPixmap(canvas)
    else:
        return

def saveFile():
    filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(MainWindow, '另存新檔', '', 'JPG(*.jpg)')
    label.pixmap().save(filePath,'JPG',90)

def closeFile():
    app.quit()

mbox = QtWidgets.QMessageBox(MainWindow)

menubar = QtWidgets.QMenuBar(MainWindow)
menu_file = QtWidgets.QMenu('檔案')
action_new = QtWidgets.QAction('開新檔案')
action_new.triggered.connect(newFile)
menu_file.addAction(action_new)
action_save = QtWidgets.QAction('另存新檔')
menu_file.addAction(action_save)
action_save.triggered.connect(saveFile)
action_close = QtWidgets.QAction('關閉')
menu_file.addAction(action_close)
action_close.triggered.connect(closeFile)
menubar.addMenu(menu_file)

MainWindow.show()
sys.exit(app.exec_())