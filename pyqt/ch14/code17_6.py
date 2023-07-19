# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys
from PIL import Image, ImageQt, ImageEnhance

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(540, 360)
        self.setUpdatesEnabled(True)
        self.img = False    # 建立一個變數儲存圖片
        self.ui()
        self.adjustUi()

    # 主要按鈕和文字標籤
    def ui(self):
        self.canvas = QPixmap(360,360)         # 建立畫布元件
        self.canvas.fill(QColor('#ffffff'))    # 預設填滿白色
        self.label = QtWidgets.QLabel(self)    # 建立 QLabel 元件，作為顯示圖片使用
        self.label.setGeometry(0, 0, 360, 360) # 設定位置和尺寸
        self.label.setPixmap(self.canvas)      # 放入畫布元件

        self.mbox = QtWidgets.QMessageBox(self)        # 建立對話視窗元件

        self.btn_open = QtWidgets.QPushButton(self)    # 開啟圖片按鈕
        self.btn_open.setText('開啟圖片')
        self.btn_open.setGeometry(400, 10, 100, 30)
        self.btn_open.clicked.connect(self.newFile)

        self.btn_save = QtWidgets.QPushButton(self)    # 另存圖片按鈕
        self.btn_save.setText('另存圖片')
        self.btn_save.setGeometry(400, 40, 100, 30)
        self.btn_save.clicked.connect(self.saveFile)

        self.btn_reset = QtWidgets.QPushButton(self)    # 重設數值按鈕
        self.btn_reset.setText('重設數值')
        self.btn_reset.setGeometry(400, 290, 100, 30)
        self.btn_reset.clicked.connect(self.resetVal)

        self.btn_close = QtWidgets.QPushButton(self)    # 關閉視窗按鈕
        self.btn_close.setText('關閉')
        self.btn_close.setGeometry(400, 320, 100, 30)
        self.btn_close.clicked.connect(self.closeFile)

    # 調整數值拉霸
    def adjustUi(self):
        self.label_adj_1 = QtWidgets.QLabel(self)       # 調整亮度說明文字
        self.label_adj_1.setGeometry(400, 80, 100, 30)
        self.label_adj_1.setText('調整亮度')
        self.label_adj_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_val_1 = QtWidgets.QLabel(self)       # 調整亮度數值
        self.label_val_1.setGeometry(500, 100, 40, 30)
        self.label_val_1.setText('0')
        self.label_val_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider_1 = QtWidgets.QSlider(self)         # 調整亮度滑桿
        self.slider_1.setOrientation(Qt.Orientation.Horizontal)
        self.slider_1.setGeometry(400,100,100,30)
        self.slider_1.setRange(-100, 100)
        self.slider_1.setValue(0)
        self.slider_1.valueChanged.connect(self.showImage)

        self.label_adj_2 = QtWidgets.QLabel(self)       # 調整對比說明文字
        self.label_adj_2.setGeometry(400, 130, 100, 30)
        self.label_adj_2.setText('調整對比')
        self.label_adj_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_val_2 = QtWidgets.QLabel(self)       # 調整對比數值
        self.label_val_2.setGeometry(500, 150, 40, 30)
        self.label_val_2.setText('0')
        self.label_val_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider_2 = QtWidgets.QSlider(self)         # 調整對比滑桿
        self.slider_2.setOrientation(Qt.Orientation.Horizontal)
        self.slider_2.setGeometry(400,150,100,30)
        self.slider_2.setRange(-100, 100)
        self.slider_2.setValue(0)
        self.slider_2.valueChanged.connect(self.showImage)

        self.label_adj_3 = QtWidgets.QLabel(self)       # 調整飽和度說明文字
        self.label_adj_3.setGeometry(400, 180, 100, 30)
        self.label_adj_3.setText('調整飽和度')
        self.label_adj_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_val_3 = QtWidgets.QLabel(self)       # 調整飽和度數值
        self.label_val_3.setGeometry(500, 200, 40, 30)
        self.label_val_3.setText('0')
        self.label_val_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.slider_3 = QtWidgets.QSlider(self)         # 調整飽和度滑桿
        self.slider_3.setOrientation(Qt.Orientation.Horizontal)
        self.slider_3.setGeometry(400,200,100,30)
        self.slider_3.setRange(-100, 100)
        self.slider_3.setValue(0)
        self.slider_3.valueChanged.connect(self.showImage)

        self.label_adj_4 = QtWidgets.QLabel(self)       # 調整銳利度說明文字
        self.label_adj_4.setGeometry(400, 230, 100, 30)
        self.label_adj_4.setText('調整銳利度')
        self.label_adj_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_val_4 = QtWidgets.QLabel(self)       # 調整銳利度數值
        self.label_val_4.setGeometry(500, 250, 40, 30)
        self.label_val_4.setText('0')

        self.slider_4 = QtWidgets.QSlider(self)         # 調整銳利度滑桿
        self.slider_4.setOrientation(Qt.Orientation.Horizontal)
        self.slider_4.setGeometry(400,250,100,30)
        self.slider_4.setRange(-100, 100)
        self.slider_4.setValue(0)
        self.slider_4.valueChanged.connect(self.showImage)

    # 開新圖片
    def newFile(self):
        global output      # 建立一個全域變數，在不同視窗之間傳遞圖片資訊
        filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='IMAGE(*.jpg *.png *.gif)')
        if filePath:
            # 如果選擇檔案，彈出視窗詢問是否開啟
            ret = self.mbox.question(self, 'question', '確定開新檔案？')
            # 如果確定開啟
            if ret == self.mbox.StandardButton.Yes:
                self.img = Image.open(filePath)                 # 使用 Pillow Image 開啟
                output = self.img                               # 紀錄圖片資訊
                qimg = ImageQt.toqimage(self.img)               # 轉換成 Qpixmap 格式
                self.canvas = QPixmap(360,360).fromImage(qimg)  # 顯示在畫布中
                self.label.setPixmap(self.canvas)               # 重設畫布內容
                self.update()                                   # 更新視窗
            else:
                return

    # 關閉
    def closeFile(self):
        ret = self.mbox.question(self, 'question', '確定關閉視窗？')
        if ret == self.mbox.StandardButton.Yes:
            app.quit()            # 如果點擊 yes，關閉視窗
        else:
            return

    # 重設
    def resetVal(self):
        self.slider_1.setValue(0)        # 滑桿預設值 0
        self.slider_2.setValue(0)        # 滑桿預設值 0
        self.slider_3.setValue(0)        # 滑桿預設值 0
        self.slider_4.setValue(0)        # 滑桿預設值 0
        self.label_val_1.setText('0')    # 滑桿數值顯示 0
        self.label_val_2.setText('0')    # 滑桿數值顯示 0
        self.label_val_3.setText('0')    # 滑桿數值顯示 0
        self.label_val_4.setText('0')    # 滑桿數值顯示 0
        qimg = ImageQt.toqimage(self.img)               # 圖片顯示 self.img 內容
        self.canvas = QPixmap(360,360).fromImage(qimg)  # 更新畫布內容
        self.label.setPixmap(self.canvas)               # 重設畫布
        self.update()                                   # 更新視窗

    # 調整並顯示圖片
    def showImage(self):
        global output
        # 如果已經開啟圖片
        if self.img != False:
            val1 = self.slider_1.value()         # 取得滑桿數值
            val2 = self.slider_2.value()         # 取得滑桿數值
            val3 = self.slider_3.value()         # 取得滑桿數值
            val4 = self.slider_4.value()         # 取得滑桿數值
            self.label_val_1.setText(str(val1))  # 顯示滑桿數值
            self.label_val_2.setText(str(val2))  # 顯示滑桿數值
            self.label_val_3.setText(str(val3))  # 顯示滑桿數值
            self.label_val_4.setText(str(val4))  # 顯示滑桿數值
            output = self.img.copy()                        # 複製 img 圖片 ( 避免更動原始圖片 )
            brightness = ImageEnhance.Brightness(output)    # 調整亮度
            output = brightness.enhance(1+int(val1)/100)    # 讀取滑桿數值並轉換成調整的數值
            contrast = ImageEnhance.Contrast(output)        # 調整對比
            output = contrast.enhance(1+int(val2)/100)      # 讀取滑桿數值並轉換成調整的數值
            color = ImageEnhance.Color(output)              # 調整飽和度
            output = color.enhance(1+int(val3)/100)         # 讀取滑桿數值並轉換成調整的數值
            sharpness = ImageEnhance.Sharpness(output)      # 調整銳利度
            output = sharpness.enhance(1+int(val4)/10)      # 讀取滑桿數值並轉換成調整的數值

            qimg = ImageQt.toqimage(output)                 # 圖片顯示 self.img 內容
            self.canvas = QPixmap(360,360).fromImage(qimg)  # 更新畫布內容
            self.label.setPixmap(self.canvas)               # 重設畫布
            self.update()                                   # 更新視窗

    def saveFile(self):
        self.nw = saveWindow()      # 連接新視窗
        self.nw.show()              # 顯示新視窗

class saveWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('選擇存檔格式')    # 新視窗標題
        self.resize(300, 180)                # 新視窗尺寸
        self.ui()

    def ui(self):
        self.label_size = QtWidgets.QLabel(self)     # 顯示尺寸縮放比例說明文字
        self.label_size.setGeometry(15, 10, 80, 30)
        self.label_size.setText('尺寸改變')

        self.imgsize =100                            # 預設圖片尺寸縮放比例

        self.box_size = QtWidgets.QSpinBox(self)     # 尺寸縮放調整元件
        self.box_size.setGeometry(15, 40, 60, 30)
        self.box_size.setRange(0,200)
        self.box_size.setValue(self.imgsize)
        self.box_size.valueChanged.connect(self.changeSize) # 串連調整函式

        self.label_format = QtWidgets.QLabel(self)   # 存檔格式說明文字
        self.label_format.setGeometry(100, 10, 100, 30)
        self.label_format.setText('儲存格式')

        self.format = 'JPG'                          # 預設格式

        self.box_format  = QtWidgets.QComboBox(self) # 下拉選單元件
        self.box_format.addItems(['JPG','PNG'])      # 兩個選項
        self.box_format.setGeometry(90,40,100,30)
        self.box_format.currentIndexChanged.connect(self.changeFormat) # 串連改變時的程式

        self.label_jpg = QtWidgets.QLabel(self)      # 壓縮品質說明文字
        self.label_jpg.setGeometry(100, 70, 100, 30)
        self.label_jpg.setText('JPG 壓縮品質')

        self.val = 75                                # 預設 JPG 壓縮品質

        self.label_jpg_val = QtWidgets.QLabel(self)  # 壓縮品質數值
        self.label_jpg_val.setGeometry(190, 100, 100, 30)
        self.label_jpg_val.setText(str(self.val))

        self.slider = QtWidgets.QSlider(self)        # 壓縮品質調整滑桿
        self.slider.setOrientation(Qt.Orientation.Horizontal)                # 水平顯示
        self.slider.setGeometry(100,100,80,30)
        self.slider.setRange(0, 100)                 # 數值範圍
        self.slider.setValue(self.val)               # 預設值
        self.slider.valueChanged.connect(self.changeVal)  # 串連改變時的函式

        self.btn_ok = QtWidgets.QPushButton(self)    # 確定儲存按鈕
        self.btn_ok.setText('確定儲存')
        self.btn_ok.setGeometry(200, 10, 90, 30)
        self.btn_ok.clicked.connect(self.saveImage)  # 串連儲存函式

        self.btn_cancel = QtWidgets.QPushButton(self)  # 取消儲存按鈕
        self.btn_cancel.setText('取消')
        self.btn_cancel.setGeometry(200, 40, 90, 30)
        self.btn_cancel.clicked.connect(self.closeWindow)  # 串連關閉視窗函式

    # 改變尺寸
    def changeSize(self):
        self.imgsize = self.box_size.value()         # 取得改變的數值

    # 改變格式
    def changeFormat(self):
        self.format = self.box_format.currentText()  # 顯示目前格式
        if self.format == 'JPG':
            self.label_jpg.setDisabled(False)        # 如果是 JPG，啟用 JPG 壓縮品質調整相關元件
            self.label_jpg_val.setDisabled(False)
            self.slider.setDisabled(False)
        else:
            self.label_jpg.setDisabled(True)        # 如果是 JPG，停用 JPG 壓縮品質調整相關元件
            self.label_jpg_val.setDisabled(True)
            self.slider.setDisabled(True)

    # 改變數值
    def changeVal(self):
        self.val = self.slider.value()              # 取得滑桿數值
        self.label_jpg_val.setText(str(self.slider.value()))

    # 存檔
    def saveImage(self):
        global output
        if self.format == 'JPG':
            filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='JPG(*.jpg)')
            if filePath:
                nw = int ( output.size[0] * self.imgsize/100 )    # 根據縮放比例調整大小
                nh = int ( output.size[1] * self.imgsize/100 )
                img2 = output.resize((nw, nh))                    # 調整大小
                img2.save(filePath, quality=self.val, subsampling=0)  # JPG 存檔
                self.close()
        else:
            filePath, filterType = QtWidgets.QFileDialog.getSaveFileName(filter='PNG(*.png)')
            if filePath:
                nw = int ( output.size[0] * self.imgsize/100 )    # 根據縮放比例調整大小
                nh = int ( output.size[1] * self.imgsize/100 )
                img2 = output.resize((nw, nh))                    # 調整大小
                img2.save(filePath, 'png')                        # PNG 存檔
                self.close()

    def closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())