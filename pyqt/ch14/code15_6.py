# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(400, 300)                # 主視窗大小

canvas = QPixmap(400,240)                  # 建立 QPixmap 元件作為畫布，並設定畫布大小
canvas.fill(QColor('#ffffff'))             # 畫布填滿白色

label = QtWidgets.QLabel(MainWindow)       # 建立 QLabel
label.setGeometry(0, 0, 400, 240)          # 設定大小位置，下方留下一些空白
label.setPixmap(canvas)                    # 放入畫布

last_x, last_y = None, None                # 設定兩個變數紀錄滑鼠座標
penSize = 10                               # 畫筆預設粗細
penColor = QColor('#000000')               # 畫筆預設顏色

# 放開滑鼠的函式
def release(self):
    global last_x, last_y
    last_x, last_y = None, None            # 清空座標內容

# 按下滑鼠的函式
def mousePress(self):
    global penColor, penSize, canvas
    mx = int(QEnterEvent.position(self).x())
    my = int(QEnterEvent.position(self).y())
    qpainter = QPainter()                  # 建立 QPainter 元件
    qpainter.begin(canvas)         # 在畫布中開始繪圖
    qpainter.setPen(QPen(QColor(penColor), penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
    qpainter.drawPoint(mx, my)             # 下筆畫出一個點
    qpainter.end()                         # 結束繪圖
    label.setPixmap(canvas)
    MainWindow.update()                    # 更新主視窗內容

# 按下滑鼠並移動滑鼠的函式
def draw(self):
    global last_x, last_y, penColor, penSize, canvas
    mx = int(QEnterEvent.position(self).x())
    my = int(QEnterEvent.position(self).y())
    if last_x is None:
        last_x = mx                 # 紀錄滑鼠當下的座標
        last_y = my
        return
    qpainter = QPainter()                  # 建立 QPainter 元件
    qpainter.begin(canvas)         # 在畫布中開始繪圖
    qpainter.setPen(QPen(penColor, penSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)) # 設定畫筆樣式
    qpainter.drawLine(last_x, last_y, mx, my) # 下筆畫出一條線
    qpainter.end()                         # 結束繪圖
    label.setPixmap(canvas) 
    MainWindow.update()                    # 更新主視窗內容
    last_x = mx                    # 紀錄結束座標
    last_y = my

label.mousePressEvent  = mousePress        # 設定按下滑鼠並移動的事件
label.mouseMoveEvent = draw                # 設定按下滑鼠的事件
label.mouseReleaseEvent = release          # 設定放開滑鼠的事件

# 點擊按鈕更換顏色函式
def changeColor(self, color):
    global penColor, btn
    penColor = QColor(color)      # 設定畫筆顏色
    for i in btn:
        btn[i].setDisabled(False) # 啟用所有按鈕
    self.setDisabled(True)        # 停用所點擊的按鈕

# 設定顏色清單
colors = ['#ff0000','#ff8800','#ffee00','#00cc00','#0066ff','#0000cc','#cc00cc','#000000','#ffffff']
btn = {}   # 因為有很多按鈕，所以使用字典方式紀錄元件
# 依序讀取顏色清單中的顏色
for i in colors:
    index = colors.index(i)   # 取得該顏色的位置 ( 按鈕定位使用 )
    btn[i] = QtWidgets.QPushButton(MainWindow) # 建立按鈕元件
    # 設定樣式，當中額外設定禁用時的樣式
    btn[i].setStyleSheet('''
        QPushButton{
            background:'''+i+''';
            margin-right:5px;
        }
        QPushButton:disabled{
            border:3px solid #000;
        }
    ''')
    btn[i].setGeometry(index*30+10,250,30,30)   # 設定每個按鈕的位置
    btn[i].clicked.connect(lambda checked, b=btn[i], c=i:  changeColor(b, c)) # 設定點擊事件

    # 切換畫筆粗細函式
    def changeSize(self, size):
        global penSize
        btn_s.setDisabled(False)  # 啟用「細」的按鈕
        btn_m.setDisabled(False)  # 啟用「中」的按鈕
        btn_l.setDisabled(False)  # 啟用「粗」的按鈕
        penSize = size            # 設定畫筆粗細
        self.setDisabled(True)    # 停用所點選的按鈕

    btn_s = QtWidgets.QPushButton(MainWindow)             # 建立「細」的按鈕
    btn_s.setText('細')
    btn_s.setGeometry(280, 250, 45, 30)                   # 設定位置
    btn_s.clicked.connect(lambda: changeSize(btn_s, 3))   # 設定點擊事件
    btn_m = QtWidgets.QPushButton(MainWindow)             # 建立「中」的按鈕
    btn_m.setText('中')
    btn_m.setGeometry(315, 250, 45, 30)                   # 設定位置
    btn_m.setDisabled(True)                               # 因為預設中，所以先停用中的按鈕
    btn_m.clicked.connect(lambda: changeSize(btn_m, 10))  # 設定點擊事件
    btn_l = QtWidgets.QPushButton(MainWindow)             # 建立「粗」的按鈕
    btn_l.setText('粗')
    btn_l.setGeometry(350, 250, 45, 30)                   # 設定位置
    btn_l.clicked.connect(lambda: changeSize(btn_l, 20))  # 設定點擊事件

# 開新檔案的函式
def newFile():
    ret = mbox.question(MainWindow, 'question', '確定開新檔案？')  # 出現對話視窗確認
    if ret == mbox.StandardButton.Yes:
        canvas.fill(QColor('#ffffff'))   # 如果按下 yes，用白色填滿畫布
        label.setPixmap(canvas)          # 重新設定畫布
    else:
        return                           # 否則就不做動作，跳出函式

# 儲存檔案的函式
def saveFile():
    filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(MainWindow, '另存新檔', '', 'JPG(*.jpg)')  # 建立開啟檔案對話視窗，設定成存檔方式
    label.pixmap().save(filePath,'JPG',90)   # 儲存為 jpg，品質 90

# 關閉的函式
def closeFile():
    app.quit()   # 結束視窗

mbox = QtWidgets.QMessageBox(MainWindow)  # 建立對話視窗
menubar = QtWidgets.QMenuBar(MainWindow)  # 建立 menubar
menu_file = QtWidgets.QMenu('檔案')        # 建立一個 File 選項 ( QMenu )
action_new = QAction('開新檔案')            # 建立一個 new 選項 ( QAction )
action_new.triggered.connect(newFile)
menu_file.addAction(action_new)            # 將 new 選項放入 File 選項裡
action_save = QAction('另存新檔')           # 建立一個 save 選項 ( QAction )
menu_file.addAction(action_save)           # 將 save 選項放入 File 選項裡
action_save.triggered.connect(saveFile)
action_close = QAction('關閉')              # 建立一個 close 選項 ( QAction )
menu_file.addAction(action_close)          # 將 close 選項放入 File 選項裡
action_close.triggered.connect(closeFile)
menubar.addMenu(menu_file)                 # 將 File 選項放入 menubar 裡

MainWindow.show()
sys.exit(app.exec())