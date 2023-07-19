# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PIL import Image

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(480, 360)

canvas = QPixmap(360,360)            # 建立 QPixmap 畫布元件
canvas.fill(QColor('#ffffff'))       # 預設填滿白色

label = QtWidgets.QLabel(MainWindow) # 建立 QLabel
label.setGeometry(0, 0, 360, 360)    # 設定大小和位置
label.setPixmap(canvas)              # 放入 QPixmap

mbox = QtWidgets.QMessageBox(MainWindow)  # 建立對話視窗元件

# 開新檔案的函式
def newFile():
    global img    # 新增全域變數 img
    # 開啟檔案時限制為 jpg、png 和 gif 的圖片格式
    filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='IMAGE(*.jpg *.png *.gif)')
    # 如果開啟檔案
    if filePath:
        ret = mbox.question(MainWindow, 'question', '確定開新檔案？')  # 彈出對話視窗詢問是否開啟
        # 如果點選 yes
        if ret == mbox.StandardButton.Yes:
            img = Image.open(filePath)       # 建立 Pillow 圖片元件紀錄圖片資訊
            canvas.load(filePath)
            label.setPixmap(canvas)    # 將圖片開啟到 QPixmap 畫布裡
            MainWindow.update()              # 更新視窗內容
        else:
            return

# 關閉視窗的函式
def closeFile():
    app.quit()

btn_open = QtWidgets.QPushButton(MainWindow)  # 開啟圖片按鈕
btn_open.setText('開啟圖片')
btn_open.setGeometry(370, 10, 100, 30)
btn_open.clicked.connect(newFile)             # 點擊按鈕的動作

btn_save = QtWidgets.QPushButton(MainWindow)  # 另存圖片按鈕
btn_save.setText('另儲圖片')
btn_save.setGeometry(370, 40, 100, 30)

btn_close = QtWidgets.QPushButton(MainWindow)  # 關閉視窗的按鈕
btn_close.setText('關閉')
btn_close.setGeometry(370, 320, 100, 30)
btn_close.clicked.connect(closeFile)           # 點擊按鈕的動作

label_size = QtWidgets.QLabel(MainWindow)   # 加入說明文字 QLabel
label_size.setGeometry(370, 70, 100, 30)
label_size.setText('尺寸改變')
label_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

size =100                    # 預設尺寸 100%
# 改變尺寸的函式
def changeSize():
    global size
    size = box_size.value()  # 取得數值調整元件的數值

box_size = QtWidgets.QSpinBox(MainWindow)  # 建立數值調整元件
box_size.setGeometry(390, 100, 60, 30)     # 設定位置
box_size.setRange(0,200)                   # 設定調整範圍
box_size.setValue(size)                    # 設定預設值
box_size.valueChanged.connect(changeSize)  # 數值改變時連動的函式

label_format = QtWidgets.QLabel(MainWindow)   # 說明文字 QLabel
label_format .setGeometry(370, 130, 100, 30)
label_format .setText('儲存格式')
label_format .setAlignment(Qt.AlignmentFlag.AlignCenter)

format = 'JPG'        # 預設壓縮格式
# 改變壓縮格式時的函式
def changeFormat():
    global format
    format = box_format.currentText()     # 取得選擇的壓縮格式
    if format == 'JPG':
        label_jpg.setDisabled(False)      # 如果是 JPG，啟用 JPG 壓縮說明文字
        label_jpg_val.setDisabled(False)  # 如果是 JPG，啟用壓縮數值顯示
        slider.setDisabled(False)         # 如果是 JPG，啟用滑桿
    else:
        label_jpg.setDisabled(True)       # 如果不是 JPG，停用 JPG 壓縮說明文字
        label_jpg_val.setDisabled(True)   # 如果不是 JPG，停用壓縮數值顯示
        slider.setDisabled(True)          # 如果不是 JPG，停用滑桿

box_format  = QtWidgets.QComboBox(MainWindow)   # 格式下拉選單
box_format .addItems(['JPG','PNG'])             # 兩種選擇格式
box_format .setGeometry(370,160,100,30)
box_format .currentIndexChanged.connect(changeFormat)  # 切換時連動函式

label_jpg = QtWidgets.QLabel(MainWindow)  # JPG 壓縮說明文字
label_jpg.setGeometry(370, 190, 100, 30)
label_jpg.setText('JPG 壓縮品質')
label_jpg.setAlignment(Qt.AlignmentFlag.AlignCenter)

val = 75   # 預設壓縮數值

label_jpg_val = QtWidgets.QLabel(MainWindow)  # 壓縮數值顯示
label_jpg_val.setGeometry(370, 210, 100, 30)
label_jpg_val.setText(str(val))
label_jpg_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

# 顯示壓縮數值的函式
def show():
    global val
    val = slider.value()     # 取得滑桿數值
    label_jpg_val.setText(str(slider.value()))  # 顯示滑桿數值

slider = QtWidgets.QSlider(MainWindow)   # 建立滑桿元件
slider.setOrientation(Qt.Orientation.Horizontal)                 # 水平顯示
slider.setGeometry(370,230,100,30)
slider.setRange(0, 100)                  # 調整範圍
slider.setValue(val)                     # 預設值
slider.valueChanged.connect(show)        # 連動壓縮數值顯示函式

# 存檔函式
def saveFile():
    global format, val, img, size
    # 如果格式為 JPG
    if format == 'JPG':
        # 限制只能存 JPG
        filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='JPG(*.jpg)')
        # 如果確定存檔
        if filePath:
            # 根據尺寸調整數值設定尺寸
            nw = int ( img.size[0] * size/100 )
            nh = int ( img.size[1] * size/100 )
            img2 = img.resize((nw, nh))
            # 使用 Pillow 函式庫存檔
            img2.save(filePath, quality=val, subsampling=0)
    else:
        # 限制只能存 PNG
        filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='PNG(*.png)')
        if filePath:
            # 根據尺寸調整數值設定尺寸
            nw = int ( img.size[0] * size/100 )
            nh = int ( img.size[1] * size/100 )
            img2 = img.resize((nw, nh))
            # 使用 Pillow 函式庫存檔
            img2.save(filePath, 'png')

def closeFile():
    app.quit()

mbox = QtWidgets.QMessageBox(MainWindow)

btn_open = QtWidgets.QPushButton(MainWindow)
btn_open.setText('開啟圖片')
btn_open.setGeometry(370, 10, 100, 30)
btn_open.clicked.connect(newFile)

btn_save = QtWidgets.QPushButton(MainWindow)
btn_save.setText('另儲圖片')
btn_save.setGeometry(370, 40, 100, 30)
btn_save.clicked.connect(saveFile)      # 連動存檔函式

MainWindow.show()
sys.exit(app.exec())