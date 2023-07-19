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

# 建立正弦波繪圖函式
def sinWave(i=0):
    fig = plt.figure(figsize=(3,2), dpi=100)
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [])
    line.set_data([], [])
    x = np.linspace(0, 2, 100)
    y = np.sin(5 * np.pi * (x - 0.01*i))
    line.set_data(x, y)
    return fig

canvas = FigureCanvas(sinWave())  # 將圖表繪製在 FigureCanvas 裡

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("oxxo.studio")
MainWindow.resize(360, 240)

graphicview = QtWidgets.QGraphicsView(MainWindow)  # 建立顯示圖片元件
graphicview.setGeometry(0, 0, 360, 240)

graphicscene = QtWidgets.QGraphicsScene()   # 建立場景
graphicscene.setSceneRect(0, 0, 340, 220)
graphicscene.addWidget(canvas)              # 場景中放入圖表

graphicview.setScene(graphicscene)          # 元件中放入場景

MainWindow.show()
sys.exit(app.exec())

