# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 300)

def show():
    filePath , filetype = QtWidgets.QFileDialog.getOpenFileName(filter='TXT (*.txt)')
    file = open(filePath,'r')      # 根據檔案路徑開啟檔案
    text = file.read()             # 讀取檔案內容
    input.setPlainText(text)       # 設定變數為檔案內容
    file.close()                   # 關閉檔案

input = QtWidgets.QPlainTextEdit(Form)  # 放入多行輸入框
input.move(10,50)

btn = QtWidgets.QPushButton(Form)
btn.move(10, 10)
btn.setText('開啟檔案')
btn.clicked.connect(show)

Form.show()
sys.exit(app.exec())

