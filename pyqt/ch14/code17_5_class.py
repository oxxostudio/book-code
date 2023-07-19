# Copyright © https://steam.oxxostudio.tw

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PIL import Image, ImageQt, ImageEnhance

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(540, 360)
        self.setUpdatesEnabled(True)
        self.img = False
        self.ui()
        self.adjustUi()

    def ui(self):
        self.canvas = QPixmap(360,360)
        self.canvas.fill(QColor('#ffffff'))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 360, 360)
        self.label.setPixmap(self.canvas)

        self.mbox = QtWidgets.QMessageBox(self)

        self.btn_open = QtWidgets.QPushButton(self)
        self.btn_open.setText('開啟圖片')
        self.btn_open.setGeometry(400, 10, 100, 30)
        self.btn_open.clicked.connect(self.newFile)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('另儲圖片')
        self.btn_save.setGeometry(400, 40, 100, 30)
        self.btn_save.clicked.connect(self.saveFile)

        self.btn_reset = QtWidgets.QPushButton(self)
        self.btn_reset.setText('重設數值')
        self.btn_reset.setGeometry(400, 290, 100, 30)
        self.btn_reset.clicked.connect(self.resetVal)

        self.btn_close = QtWidgets.QPushButton(self)
        self.btn_close.setText('關閉')
        self.btn_close.setGeometry(400, 320, 100, 30)
        self.btn_close.clicked.connect(self.closeFile)

    def newFile(self):
        global output
        filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='IMAGE(*.jpg *.png *.gif)')
        if filePath:
            ret = self.mbox.question(self, 'question', '確定開新檔案？')
            if ret == self.mbox.Yes:
                self.img = Image.open(filePath)
                output = self.img
                qimg = ImageQt.toqimage(self.img)
                self.canvas = QPixmap(360,360).fromImage(qimg)
                self.label.setPixmap(self.canvas)
                self.update()
            else:
                return

    def saveFile(self):
        self.nw = saveWindow()       # 連接新視窗
        self.nw.show()              # 顯示新視窗

    def closeFile(self):
        ret = self.mbox.question(self, 'question', '確定關閉視窗？')
        if ret == self.mbox.Yes:
            app.quit()
        else:
            return

    def adjustUi(self):
        self.label_adj_1 = QtWidgets.QLabel(self)
        self.label_adj_1.setGeometry(400, 80, 100, 30)
        self.label_adj_1.setText('調整亮度')
        self.label_adj_1.setAlignment(Qt.AlignCenter)

        self.label_val_1 = QtWidgets.QLabel(self)
        self.label_val_1.setGeometry(500, 100, 40, 30)
        self.label_val_1.setText('0')
        self.label_val_1.setAlignment(Qt.AlignCenter)

        self.slider_1 = QtWidgets.QSlider(self)
        self.slider_1.setOrientation(1)
        self.slider_1.setGeometry(400,100,100,30)
        self.slider_1.setRange(-100, 100)
        self.slider_1.setValue(0)
        self.slider_1.valueChanged.connect(self.showImage)

        self.label_adj_2 = QtWidgets.QLabel(self)
        self.label_adj_2.setGeometry(400, 130, 100, 30)
        self.label_adj_2.setText('調整對比')
        self.label_adj_2.setAlignment(Qt.AlignCenter)

        self.label_val_2 = QtWidgets.QLabel(self)
        self.label_val_2.setGeometry(500, 150, 40, 30)
        self.label_val_2.setText('0')
        self.label_val_2.setAlignment(Qt.AlignCenter)

        self.slider_2 = QtWidgets.QSlider(self)
        self.slider_2.setOrientation(1)
        self.slider_2.setGeometry(400,150,100,30)
        self.slider_2.setRange(-100, 100)
        self.slider_2.setValue(0)
        self.slider_2.valueChanged.connect(self.showImage)

        self.label_adj_3 = QtWidgets.QLabel(self)
        self.label_adj_3.setGeometry(400, 180, 100, 30)
        self.label_adj_3.setText('調整飽和度')
        self.label_adj_3.setAlignment(Qt.AlignCenter)

        self.label_val_3 = QtWidgets.QLabel(self)
        self.label_val_3.setGeometry(500, 200, 40, 30)
        self.label_val_3.setText('0')
        self.label_val_3.setAlignment(Qt.AlignCenter)

        self.slider_3 = QtWidgets.QSlider(self)
        self.slider_3.setOrientation(1)
        self.slider_3.setGeometry(400,200,100,30)
        self.slider_3.setRange(-100, 100)
        self.slider_3.setValue(0)
        self.slider_3.valueChanged.connect(self.showImage)

        self.label_adj_4 = QtWidgets.QLabel(self)
        self.label_adj_4.setGeometry(400, 230, 100, 30)
        self.label_adj_4.setText('調整銳利度')
        self.label_adj_4.setAlignment(Qt.AlignCenter)

        self.label_val_4 = QtWidgets.QLabel(self)
        self.label_val_4.setGeometry(500, 250, 40, 30)
        self.label_val_4.setText('0')
        self.label_val_4.setAlignment(Qt.AlignCenter)

        self.slider_4 = QtWidgets.QSlider(self)
        self.slider_4.setOrientation(1)
        self.slider_4.setGeometry(400,250,100,30)
        self.slider_4.setRange(-100, 100)
        self.slider_4.setValue(0)
        self.slider_4.valueChanged.connect(self.showImage)

    def resetVal(self):
        self.slider_1.setValue(0)
        self.slider_2.setValue(0)
        self.slider_3.setValue(0)
        self.slider_4.setValue(0)
        self.label_val_1.setText('0')
        self.label_val_2.setText('0')
        self.label_val_3.setText('0')
        self.label_val_4.setText('0')
        qimg = ImageQt.toqimage(self.img)
        self.canvas = QPixmap(360,360).fromImage(qimg)
        self.label.setPixmap(self.canvas)
        self.update()

    def showImage(self):
        global output
        if self.img != False:
            val1 = self.slider_1.value()
            val2 = self.slider_2.value()
            val3 = self.slider_3.value()
            val4 = self.slider_4.value()
            self.label_val_1.setText(str(val1))
            self.label_val_2.setText(str(val2))
            self.label_val_3.setText(str(val3))
            self.label_val_4.setText(str(val4))
            output = self.img.copy()
            brightness = ImageEnhance.Brightness(output)
            output = brightness.enhance(1+int(val1)/100)
            contrast = ImageEnhance.Contrast(output)
            output = contrast.enhance(1+int(val2)/100)
            color = ImageEnhance.Color(output)
            output = color.enhance(1+int(val3)/100)
            sharpness = ImageEnhance.Sharpness(output)
            output = sharpness.enhance(1+int(val4)/10)

            qimg = ImageQt.toqimage(output)
            self.canvas = QPixmap(360,360).fromImage(qimg)
            self.label.setPixmap(self.canvas)
            self.update()

class saveWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('選擇存檔格式')
        self.resize(300, 180)
        self.ui()

    def ui(self):
        self.label_size = QtWidgets.QLabel(self)
        self.label_size.setGeometry(15, 10, 80, 30)
        self.label_size.setText('尺寸改變')

        self.imgsize =100

        self.box_size = QtWidgets.QSpinBox(self)
        self.box_size.setGeometry(15, 40, 60, 30)
        self.box_size.setRange(0,200)
        self.box_size.setValue(self.imgsize)
        self.box_size.valueChanged.connect(self.changeSize)

        self.label_format = QtWidgets.QLabel(self)
        self.label_format.setGeometry(100, 10, 100, 30)
        self.label_format.setText('儲存格式')

        self.format = 'JPG'

        self.box_format  = QtWidgets.QComboBox(self)
        self.box_format.addItems(['JPG','PNG'])
        self.box_format.setGeometry(90,40,100,30)
        self.box_format.currentIndexChanged.connect(self.changeFormat)

        self.label_jpg = QtWidgets.QLabel(self)
        self.label_jpg.setGeometry(100, 70, 100, 30)
        self.label_jpg.setText('JPG 壓縮品質')

        self.val = 75

        self.label_jpg_val = QtWidgets.QLabel(self)
        self.label_jpg_val.setGeometry(190, 100, 100, 30)
        self.label_jpg_val.setText(str(self.val))

        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(1)
        self.slider.setGeometry(100,100,80,30)
        self.slider.setRange(0, 100)
        self.slider.setValue(self.val)
        self.slider.valueChanged.connect(self.changeVal)

        self.btn_ok = QtWidgets.QPushButton(self)
        self.btn_ok.setText('確定儲存')
        self.btn_ok.setGeometry(200, 10, 90, 30)
        self.btn_ok.clicked.connect(self.saveImage)

        self.btn_cancel = QtWidgets.QPushButton(self)
        self.btn_cancel.setText('取消')
        self.btn_cancel.setGeometry(200, 40, 90, 30)
        self.btn_cancel.clicked.connect(self.closeWindow)

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

    def changeVal(self):
        self.val = self.slider.value()
        self.label_jpg_val.setText(str(self.slider.value()))

    def saveImage(self):
        global output
        if self.format == 'JPG':
            filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='JPG(*.jpg)')
            if filePath:
                nw = int ( output.size[0] * self.imgsize/100 )
                nh = int ( output.size[1] * self.imgsize/100 )
                img2 = output.resize((nw, nh))
                img2.save(filePath, quality=self.val, subsampling=0)
                self.close()
        else:
            filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='PNG(*.png)')
            if filePath:
                nw = int ( output.size[0] * self.imgsize/100 )
                nh = int ( output.size[1] * self.imgsize/100 )
                img2 = output.resize((nw, nh))
                img2.save(filePath, 'png')
                self.close()

    def closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())