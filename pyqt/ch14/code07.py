# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
import sys
import zipfile

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(400, 300)

fileList = []

def open():
    filePath , filterType = QtWidgets.QFileDialog.getOpenFileNames()
    print(filePath , filterType)
    for i in filePath:
        if i not in fileList:
            fileList.append(i)
    output = '\n'.join(fileList)
    input.setText(output)

def zipFile():
    zf = zipfile.ZipFile('test.zip', mode='w')  # 建立壓縮檔
    for i in fileList:
        zf.write(i)     # 檔案寫入壓縮檔
    zf.close()          # 關閉壓縮檔

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('選擇檔案')
btn1.setGeometry(20,5,80,35)
btn1.clicked.connect(open)

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('壓縮存檔')
btn2.setGeometry(300,5,80,35)
btn1.clicked.connect(zipFile)  # 點擊按鈕時執行壓縮的函式

input = QtWidgets.QTextEdit(Form)
input.setGeometry(20,40,360,240)
input.setLineWrapMode(input.LineWrapMode.NoWrap)

Form.show()
sys.exit(app.exec())

