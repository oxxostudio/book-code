# Copyright © https://steam.oxxostudio.tw

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor, QFont
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)

    def paintEvent(self, event):
        qpainter = QPainter()
        qpainter.begin(self)

        font = QFont()            # 建立文字樣式物件
        font.setWeight(87)        # 設定文字粗細
        font.setPointSize(50)     # 設定文字大小
        font.setFamily('Times')   # 設定字型
        font.setStyle(QFont.StyleItalic)  # 設定文字樣式
        # font.setStyle(QFont.StyleItalic)  # PyQt5 寫法

        qpainter.setPen(QColor('#ff0000'))
        qpainter.setFont(font)    # 根據文字樣式物件設定文字樣式
        qpainter.drawText(50,50,'hello')  # 放入文字

        qpainter.setPen(QColor('#0000ff'))
        qpainter.setFont(QFont('Arial',30)) # 直接使用 QFont 設定文字樣式
        qpainter.drawText(50,100,'hello')   # 放入文字

        qpainter.end()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())

