# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
import sys
import zipfile

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(400, 300)

fileList = []   # 建立最後檔案清單

def open():
    filePath , filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選擇檔案對話視窗
    print(filePath , filterType)
    # 如果檔案清單裡沒有開啟的檔案，就將檔案路徑存入清單中
    for i in filePath:
        if i not in fileList:
            fileList.append(i)         # 將開啟的檔案添加到輸出清單裡
    output = '\n'.join(fileList)      # 使用換行符號，合併檔案清單為文字
    input.setText(output)             # 多行輸入框中顯示文字

btn1 = QtWidgets.QPushButton(Form)    # 在 Form 中加入一個 QPushButton
btn1.setText('選擇檔案')               # 按鈕文字
btn1.setGeometry(20,5,80,35)
btn1.clicked.connect(open)

input = QtWidgets.QTextEdit(Form)     # QTextEdit 多行輸入框
input.setGeometry(20,40,360,240)
input.setLineWrapMode(input.LineWrapMode.NoWrap) # 設定不要自動換行，除非遇到換行符號

Form.show()
sys.exit(app.exec())

