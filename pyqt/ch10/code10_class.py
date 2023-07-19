# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets
import sys

class mainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('測試文字')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('開啟新視窗')
        self.btn.setStyleSheet('font-size:16px;')
        self.btn.setGeometry(40,60,120,40)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = mainWindow()
    Form.show()
    sys.exit(app.exec())

