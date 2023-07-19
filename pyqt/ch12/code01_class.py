# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor, QPen
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)

    # 定義 paintEvent 屬性，注意需要包含 self 和 event 參數
    def paintEvent(self, event):
        qpainter = QPainter()          # 建立繪圖器
        qpainter.begin(self)           # 在 MainWindow 開始繪圖

        qpainter.setPen(QPen(QColor('#ff0000'),5))  # 設定畫筆顏色和寬度
        qpainter.drawRect(50, 50, 100, 100)  # 繪製正方形

        qpainter.end()                       # 結束繪圖

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

