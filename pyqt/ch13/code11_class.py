# Copyright © https://steam.oxxostudio.tw

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")  # 使用 Qt5

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(360, 240)
        self.t = 0
        self.ui()

    def ui(self):
        self.canvas = FigureCanvas(self.sinWave())

        self.graphicview = QtWidgets.QGraphicsView(self)
        self.graphicview.setGeometry(0, 0, 360, 240)

        self.graphicscene = QtWidgets.QGraphicsScene()
        self.graphicscene.setSceneRect(0, 0, 340, 220)
        self.graphicscene.addWidget(self.canvas)

        self.graphicview.setScene(self.graphicscene)

    def sinWave(self, i=0):
        fig = plt.figure(figsize=(3,2), dpi=100)
        ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
        line, = ax.plot([], [])
        line.set_data([], [])
        x = np.linspace(0, 2, 100)
        y = np.sin(5 * np.pi * (x - 0.01*i))
        line.set_data(x, y)
        plt.close()
        return fig

    def count(self):
        self.t = self.t + 5
        self.canvas = FigureCanvas(self.sinWave(self.t))
        self.graphicscene.clear()
        self.graphicscene.addWidget(self.canvas)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()

    timer = QTimer()                    # 加入定時器
    timer.timeout.connect(Form.count)   # 設定定時要執行的 function
    timer.start(50)                     # 啟用定時器，設定間隔時間為 500 毫秒
    sys.exit(app.exec())

