# Copyright © https://steam.oxxostudio.tw

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PIL import Image

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(480, 360)

canvas = QPixmap(360,360)
canvas.fill(QColor('#ffffff'))

label = QtWidgets.QLabel(MainWindow)
label.setGeometry(0, 0, 360, 360)
label.setPixmap(canvas)

def newFile():
    global img
    filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='IMAGE(*.jpg *.png *.gif)')
    if filePath:
        ret = mbox.question(MainWindow, 'question', '確定開新檔案？')
        if ret == mbox.Yes:
            img = Image.open(filePath)
            label.pixmap().load(filePath)
            MainWindow.update()
        else:
            return

def saveFile():
    global format, val, img, size
    if format == 'JPG':
        filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='JPG(*.jpg)')
        if filePath:
            nw = int ( img.size[0] * size/100 )
            nh = int ( img.size[1] * size/100 )
            img2 = img.resize((nw, nh))
            img2.save(filePath, quality=val, subsampling=0)
    else:
        filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='PNG(*.png)')
        if filePath:
            nw = int ( img.size[0] * size/100 )
            nh = int ( img.size[1] * size/100 )
            img2 = img.resize((nw, nh))
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
btn_save.clicked.connect(saveFile)

btn_close = QtWidgets.QPushButton(MainWindow)
btn_close.setText('關閉')
btn_close.setGeometry(370, 320, 100, 30)
btn_close.clicked.connect(closeFile)

label_size = QtWidgets.QLabel(MainWindow)
label_size.setGeometry(370, 70, 100, 30)
label_size.setText('尺寸改變')
label_size.setAlignment(Qt.AlignCenter)

size =100
def changeSize():
    global size
    size = box_size.value()

box_size = QtWidgets.QSpinBox(MainWindow)
box_size.setGeometry(390, 100, 60, 30)
box_size.setRange(0,200)
box_size.setValue(size)
box_size.valueChanged.connect(changeSize)


label_format = QtWidgets.QLabel(MainWindow)
label_format .setGeometry(370, 130, 100, 30)
label_format .setText('儲存格式')
label_format .setAlignment(Qt.AlignCenter)

format = 'JPG'

def changeFormat():
    global format
    format = box_format.currentText()
    if format == 'JPG':
        label_jpg.setDisabled(False)
        label_jpg_val.setDisabled(False)
        slider.setDisabled(False)
    else:
        label_jpg.setDisabled(True)
        label_jpg_val.setDisabled(True)
        slider.setDisabled(True)

box_format  = QtWidgets.QComboBox(MainWindow)
box_format .addItems(['JPG','PNG'])
box_format .setGeometry(370,160,100,30)
box_format .currentIndexChanged.connect(changeFormat)

label_jpg = QtWidgets.QLabel(MainWindow)
label_jpg.setGeometry(370, 190, 100, 30)
label_jpg.setText('JPG 壓縮品質')
label_jpg.setAlignment(Qt.AlignCenter)

val = 75

label_jpg_val = QtWidgets.QLabel(MainWindow)
label_jpg_val.setGeometry(370, 210, 100, 30)
label_jpg_val.setText(str(val))
label_jpg_val.setAlignment(Qt.AlignCenter)

def show():
    global val
    val = slider.value()
    label_jpg_val.setText(str(slider.value()))

slider = QtWidgets.QSlider(MainWindow)
slider.setOrientation(1)
slider.setGeometry(370,230,100,30)
slider.setRange(0, 100)
slider.setValue(val)
slider.valueChanged.connect(show)

MainWindow.show()
sys.exit(app.exec_())