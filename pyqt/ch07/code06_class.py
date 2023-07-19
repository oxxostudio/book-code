# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        self.btn = QtWidgets.QPushButton(self)  # 加入按鈕
        self.btn.move(20, 20)
        self.btn.setText('開啟檔案')
        self.btn.clicked.connect(self.open)

    def open(self):
        filePath , filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選擇檔案對話視窗
        print(filePath , filterType)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

