# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 300)
        self.ui()

    def ui(self):
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText('彈出視窗')
        self.btn.clicked.connect(self.showBox)        # 點擊按鈕執行函式

    def showBox(self):
        self.mbox = QtWidgets.QMessageBox(self)       # 加入對話視窗
        self.mbox.information(self, 'info', 'hello')  # 開啟資訊通知的對話視窗，標題 info，內容 hello

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

