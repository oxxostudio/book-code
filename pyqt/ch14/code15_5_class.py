# Copyright © https://steam.oxxostudio.tw

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(400, 300)
        self.ui()
        self.colorBtn()
        self.sizeBtn()
        self.menubar()

    def ui(self):
        self.last_x, self.last_y = None, None
        self.penSize = 10
        self.penColor = QColor('#000000')
        self.canvas = QPixmap(400,240)
        self.canvas.fill(QColor('#ffffff'))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 400, 240)
        self.label.setPixmap(self.canvas)

    def mousePressEvent(self, event):
        qpainter = QPainter()
        qpainter.begin(self.label.pixmap())
        qpainter.setPen(QPen(QColor(self.penColor), self.penSize, Qt.SolidLine, Qt.RoundCap))
        qpainter.drawPoint(event.x(), event.y())
        qpainter.end()
        self.update()

    def mouseMoveEvent(self, event):
        if self.last_x is None:
            self.last_x = event.x()
            self.last_y = event.y()
            return
        qpainter = QPainter()
        qpainter.begin(self.label.pixmap())
        qpainter.setPen(QPen(self.penColor, self.penSize, Qt.SolidLine, Qt.RoundCap))
        qpainter.drawLine(self.last_x, self.last_y, event.x(), event.y())
        qpainter.end()
        self.update()
        self.last_x = event.x()
        self.last_y = event.y()

    def mouseReleaseEvent(self, event):
        self.last_x, self.last_y = None, None


    def colorBtn(self):
        colors = ['#ff0000','#ff8800','#ffee00','#00cc00','#0066ff','#0000cc','#cc00cc','#000000','#ffffff']
        self.btn = {}
        for i in colors:
            index = colors.index(i)
            self.btn[i] = QtWidgets.QPushButton(self)
            self.btn[i].setStyleSheet('''
                QPushButton{
                    background:'''+i+''';
                    margin-right:5px;
                }
                QPushButton:disabled{
                    border:3px solid #000;
                }
            ''')
            self.btn[i].colorIndex = index
            self.btn[i].setGeometry(index*30+10,250,30,30)
            self.btn[i].clicked.connect(lambda checked, b=self.btn[i],c=i:  self.changeColor(b, c))

    def changeColor(self, thisBtn, color):
        self.penColor = QColor(color)
        for i in self.btn:
            self.btn[i].setDisabled(False)
        thisBtn.setDisabled(True)

    def sizeBtn(self):
        self.btn_s = QtWidgets.QPushButton(self)
        self.btn_s.setText('細')
        self.btn_s.setGeometry(280, 250, 45, 30)
        self.btn_s.clicked.connect(lambda: self.changeSize(self.btn_s, 3))
        self.btn_m = QtWidgets.QPushButton(self)
        self.btn_m.setText('中')
        self.btn_m.setGeometry(315, 250, 45, 30)
        self.btn_m.setDisabled(True)
        self.btn_m.clicked.connect(lambda: self.changeSize(self.btn_m, 10))
        self.btn_l = QtWidgets.QPushButton(self)
        self.btn_l.setText('粗')
        self.btn_l.setGeometry(350, 250, 45, 30)
        self.btn_l.clicked.connect(lambda: self.changeSize(self.btn_l, 20))

    def changeSize(self, thisBtn, size):
        self.btn_s.setDisabled(False)
        self.btn_m.setDisabled(False)
        self.btn_l.setDisabled(False)
        self.penSize = size
        thisBtn.setDisabled(True)


    def menubar(self):
        self.mbox = QtWidgets.QMessageBox(self)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menu_file = QtWidgets.QMenu('檔案')
        self.action_new = QtWidgets.QAction('開新檔案')
        self.action_new.triggered.connect(self.newFile)
        self.menu_file.addAction(self.action_new)
        self.action_save = QtWidgets.QAction('另存新檔')
        self.menu_file.addAction(self.action_save)
        self.action_save.triggered.connect(self.saveFile)
        self.action_close = QtWidgets.QAction('關閉')
        self.menu_file.addAction(self.action_close)
        self.action_close.triggered.connect(self.closeFile)
        self.menubar.addMenu(self.menu_file)

    def newFile(self):
        ret = self.mbox.question(self, 'question', '確定開新檔案？')
        if ret == self.mbox.Yes:
            self.canvas.fill(QColor('#ffffff'))
            self.label.setPixmap(self.canvas)
        else:
            return

    def saveFile(self):
        filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(self, '另存新檔', '', 'JPG(*.jpg)')  # 選取多個檔案
        self.label.pixmap().save(filePath,'JPG',90)   # 儲存為 jpg

    def closeFile(self):
        app.quit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())