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

def sinWave(i=0):
    plt.close()     # 執行時先刪除已有的 plt
    fig = plt.figure(figsize=(3,2), dpi=100)
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [])
    line.set_data([], [])
    x = np.linspace(0, 2, 100)
    y = np.sin(5 * np.pi * (x - 0.01*i))
    line.set_data(x, y)
    return fig

canvas = FigureCanvas(sinWave())

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(360, 240)

graphicview = QtWidgets.QGraphicsView(MainWindow)
graphicview.setGeometry(0, 0, 360, 240)

graphicscene = QtWidgets.QGraphicsScene()
graphicscene.setSceneRect(0, 0, 340, 220)
graphicscene.addWidget(canvas)

graphicview.setScene(graphicscene)

dx = 0   # x 位移初始值

def count():
    global dx, canvas
    dx = dx + 5                         # 每次定時器執行位移 5
    canvas = FigureCanvas(sinWave(dx))  # 產生新的正弦波圖形
    graphicscene.clear()                # 清空場景
    graphicscene.addWidget(canvas)      # 場景放入圖形

timer = QTimer()                        # 加入定時器
timer.timeout.connect(count)            # 設定定時要執行的 function
timer.start(50)                         # 啟用定時器，設定間隔時間為 500 毫秒

MainWindow.show()
sys.exit(app.exec())

