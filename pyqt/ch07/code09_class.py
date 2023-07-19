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
        self.input = QtWidgets.QPlainTextEdit(self)  # 放入多行輸入框
        self.input.move(10,50)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText('開啟檔案')
        self.btn.clicked.connect(self.showText)

    def showText(self):
        filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='TXT (*.txt)')
        file = open(filePath,'r')      # 根據檔案路徑開啟檔案
        text = file.read()             # 讀取檔案內容
        self.input.setPlainText(text)       # 設定變數為檔案內容
        file.close()                   # 關閉檔案

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

