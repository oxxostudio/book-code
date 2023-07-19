# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PIL import Image

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(480, 360)
        self.ui()
        self.resizeUi()
        self.formatUi()

    def ui(self):
        self.canvas = QPixmap(360,360)
        self.canvas.fill(QColor('#ffffff'))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 360, 360)
        self.label.setPixmap(self.canvas)

        self.mbox = QtWidgets.QMessageBox(self)

        self.btn_open = QtWidgets.QPushButton(self)
        self.btn_open.setText('開啟圖片')
        self.btn_open.setGeometry(370, 10, 100, 30)
        self.btn_open.clicked.connect(self.newFile)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('另儲圖片')
        self.btn_save.setGeometry(370, 40, 100, 30)
        self.btn_save.clicked.connect(self.saveFile)

        self.btn_close = QtWidgets.QPushButton(self)
        self.btn_close.setText('關閉')
        self.btn_close.setGeometry(370, 320, 100, 30)
        self.btn_close.clicked.connect(self.closeFile)

    def resizeUi(self):
        self.imgsize =100
        self.label_size = QtWidgets.QLabel(self)
        self.label_size.setGeometry(370, 70, 100, 30)
        self.label_size.setText('尺寸改變')
        self.label_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.box_size = QtWidgets.QSpinBox(self)
        self.box_size.setGeometry(390, 100, 60, 30)
        self.box_size.setRange(0,200)
        self.box_size.setValue(self.imgsize)
        self.box_size.valueChanged.connect(self.changeSize)

    def formatUi(self):
        self.label_format = QtWidgets.QLabel(self)
        self.label_format .setGeometry(370, 130, 100, 30)
        self.label_format .setText('儲存格式')
        self.label_format .setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.format = 'JPG'

        self.box_format  = QtWidgets.QComboBox(self)
        self.box_format .addItems(['JPG','PNG'])
        self.box_format .setGeometry(370,160,100,30)
        self.box_format .currentIndexChanged.connect(self.changeFormat)

        self.label_jpg = QtWidgets.QLabel(self)
        self.label_jpg.setGeometry(370, 190, 100, 30)
        self.label_jpg.setText('JPG 壓縮品質')
        self.label_jpg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.val = 75

        self.label_jpg_val = QtWidgets.QLabel(self)
        self.label_jpg_val.setGeometry(370, 210, 100, 30)
        self.label_jpg_val.setText(str(self.val))
        self.label_jpg_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setGeometry(370,230,100,30)
        self.slider.setRange(0, 100)
        self.slider.setValue(self.val)
        self.slider.valueChanged.connect(self.showVal)

    def newFile(self):
        filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='IMAGE(*.jpg *.png *.gif)')
        if filePath:
            ret = self.mbox.question(self, 'question', '確定開新檔案？')
            if ret == self.mbox.StandardButton.Yes:
                self.img = Image.open(filePath)
                self.canvas.load(filePath)
                self.label.setPixmap(self.canvas)    # 將圖片開啟到 QPixmap 畫布裡
                self.update()
            else:
                return

    def saveFile(self):
        if self.format == 'JPG':
            filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='JPG(*.jpg)')
            if filePath:
                nw = int ( self.img.size[0] * self.imgsize/100 )
                nh = int ( self.img.size[1] * self.imgsize/100 )
                img2 = self.img.resize((nw, nh))
                img2.save(filePath, quality=self.val, subsampling=0)
        else:
            filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='PNG(*.png)')
            if filePath:
                nw = int ( self.img.size[0] * self.imgsize/100 )
                nh = int ( self.img.size[1] * self.imgsize/100 )
                img2 = self.img.resize((nw, nh))
                img2.save(filePath, 'png')

    def closeFile(self):
        app.quit()

    def changeSize(self):
        self.imgsize = self.box_size.value()

    def changeFormat(self):
        self.format = self.box_format.currentText()
        if self.format == 'JPG':
            self.label_jpg.setDisabled(False)
            self.label_jpg_val.setDisabled(False)
            self.slider.setDisabled(False)
        else:
            self.label_jpg.setDisabled(True)
            self.label_jpg_val.setDisabled(True)
            self.slider.setDisabled(True)

    def showVal(self):
        self.val = self.slider.value()
        self.label_jpg_val.setText(str(self.slider.value()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())