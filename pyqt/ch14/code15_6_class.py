# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(400, 300)
        self.setUpdatesEnabled(True)
        self.last_x, self.last_y = None, None   # 設定兩個變數紀錄滑鼠座標
        self.penSize = 10                       # 畫筆預設粗細
        self.penColor = QColor('#000000')       # 畫筆預設顏色
        self.ui()

    def ui(self):
        self.canvas = QPixmap(400,240)            # 建立 QPixmap 元件作為畫布，並設定畫布大小
        self.canvas.fill(QColor('#ffffff'))       # 畫布填滿白色

        self.label = QtWidgets.QLabel(self)       # 建立 QLabel
        self.label.setGeometry(0, 0, 400, 240)    # 設定大小位置，下方留下一些空白
        self.label.setPixmap(self.canvas)         # 放入畫布

        # 設定顏色清單
        self.colors = ['#ff0000','#ff8800','#ffee00','#00cc00','#0066ff','#0000cc','#cc00cc','#000000','#ffffff']
        self.btn = {}   # 因為有很多按鈕，所以使用字典方式紀錄元件
        # 依序讀取顏色清單中的顏色
        for i in self.colors:
            index = self.colors.index(i)   # 取得該顏色的位置 ( 按鈕定位使用 )
            self.btn[i] = QtWidgets.QPushButton(self) # 建立按鈕元件
            # 設定樣式，當中額外設定禁用時的樣式
            self.btn[i].setStyleSheet('''
                QPushButton{
                    background:'''+i+''';
                    margin-right:5px;
                }
                QPushButton:disabled{
                    border:3px solid #000;
                }
            ''')
            self.btn[i].setGeometry(index*30+10,250,30,30)   # 設定每個按鈕的位置
            self.btn[i].clicked.connect(lambda checked, b=self.btn[i], c=i:  self.changeColor(b, c)) # 設定點擊事件

            self.btn_s = QtWidgets.QPushButton(self)             # 建立「細」的按鈕
            self.btn_s.setText('細')
            self.btn_s.setGeometry(280, 250, 45, 30)                   # 設定位置
            self.btn_s.clicked.connect(lambda: self.changeSize(self.btn_s, 3))   # 設定點擊事件
            self.btn_m = QtWidgets.QPushButton(self)             # 建立「中」的按鈕
            self.btn_m.setText('中')
            self.btn_m.setGeometry(315, 250, 45, 30)                   # 設定位置
            self.btn_m.setDisabled(True)                               # 因為預設中，所以先停用中的按鈕
            self.btn_m.clicked.connect(lambda: self.changeSize(self.btn_m, 10))  # 設定點擊事件
            self.btn_l = QtWidgets.QPushButton(self)             # 建立「粗」的按鈕
            self.btn_l.setText('粗')
            self.btn_l.setGeometry(350, 250, 45, 30)                   # 設定位置
            self.btn_l.clicked.connect(lambda: self.changeSize(self.btn_l, 20))  # 設定點擊事件

        self.mbox = QtWidgets.QMessageBox(self)  # 建立對話視窗
        self.menubar = QtWidgets.QMenuBar(self)  # 建立 menubar
        self.menu_file = QtWidgets.QMenu('檔案')        # 建立一個 File 選項 ( QMenu )
        self.action_new = QAction('開新檔案')            # 建立一個 new 選項 ( QAction )
        self.action_new.triggered.connect(self.newFile)
        self.menu_file.addAction(self.action_new)            # 將 new 選項放入 File 選項裡
        self.action_save = QAction('另存新檔')           # 建立一個 save 選項 ( QAction )
        self.menu_file.addAction(self.action_save)           # 將 save 選項放入 File 選項裡
        self.action_save.triggered.connect(self.saveFile)
        self.action_close = QAction('關閉')              # 建立一個 close 選項 ( QAction )
        self.menu_file.addAction(self.action_close)          # 將 close 選項放入 File 選項裡
        self.action_close.triggered.connect(self.closeFile)
        self.menubar.addMenu(self.menu_file)                 # 將 File 選項放入 menubar 裡

    def mousePressEvent(self, event):
        mx = int(QEnterEvent.position(event).x())
        my = int(QEnterEvent.position(event).y())
        qpainter = QPainter()                  # 建立 QPainter 元件
        qpainter.begin(self.canvas)         # 在畫布中開始繪圖
        qpainter.setPen(QPen(QColor(self.penColor), self.penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
        qpainter.drawPoint(mx, my)             # 下筆畫出一個點
        qpainter.end()                         # 結束繪圖
        self.label.setPixmap(self.canvas)
        self.update()                    # 更新主視窗內容

    def mouseMoveEvent(self, event):
        mx = int(QEnterEvent.position(event).x())
        my = int(QEnterEvent.position(event).y())
        if self.last_x is None:
            self.last_x = mx                 # 紀錄滑鼠當下的座標
            self.last_y = my
            return
        qpainter = QPainter()               # 建立 QPainter 元件
        qpainter.begin(self.canvas)         # 在畫布中開始繪圖
        qpainter.setPen(QPen(self.penColor, self.penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
        qpainter.drawLine(self.last_x, self.last_y, mx, my) # 下筆畫出一條線
        qpainter.end()                      # 結束繪圖
        self.label.setPixmap(self.canvas)
        self.update()                       # 更新主視窗內容
        self.last_x = mx                    # 紀錄結束座標
        self.last_y = my

    def mouseReleaseEvent(self, event):
        self.last_x, self.last_y = None, None  # 清空座標內容

    # 點擊按鈕更換顏色函式
    def changeColor(self, thisBtn, color):
        self.penColor = QColor(color)      # 設定畫筆顏色
        for i in self.btn:
            self.btn[i].setDisabled(False) # 啟用所有按鈕
        thisBtn.setDisabled(True)          # 停用所點擊的按鈕

    def changeSize(self, thisBtn, size):
        self.btn_s.setDisabled(False)  # 啟用「細」的按鈕
        self.btn_m.setDisabled(False)  # 啟用「中」的按鈕
        self.btn_l.setDisabled(False)  # 啟用「粗」的按鈕
        self.penSize = size            # 設定畫筆粗細
        thisBtn.setDisabled(True)    # 停用所點選的按鈕

    # 開新檔案的函式
    def newFile(self):
        ret = self.mbox.question(self, 'question', '確定開新檔案？')  # 出現對話視窗確認
        if ret == self.mbox.StandardButton.Yes:
            self.canvas.fill(QColor('#ffffff'))   # 如果按下 yes，用白色填滿畫布
            self.label.setPixmap(self.canvas)          # 重新設定畫布
        else:
            return                           # 否則就不做動作，跳出函式

    # 儲存檔案的函式
    def saveFile(self):
        filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(self, '另存新檔', '', 'JPG(*.jpg)')  # 建立開啟檔案對話視窗，設定成存檔方式
        self.label.pixmap().save(filePath,'JPG',90)   # 儲存為 jpg，品質 90

    # 關閉的函式
    def closeFile(self):
        app.quit()   # 結束視窗


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())