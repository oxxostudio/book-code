# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def openFiles():
    filePath, filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選取多個檔案
    print(filePath, filterType )

def openFolder():
    folderPath = QtWidgets.QFileDialog.getExistingDirectory()        # 選取特定資料夾
    print(folderPath)

btn1 = QtWidgets.QPushButton(Form)
btn1.move(20, 20)
btn1.setText('開啟檔案')
btn1.clicked.connect(openFiles)     # 點擊執行開啟檔案函式

btn2 = QtWidgets.QPushButton(Form)
btn2.move(120, 20)
btn2.setText('開啟資料夾')
btn2.clicked.connect(openFolder)    # 點擊執行開啟資料夾函式

Form.show()
sys.exit(app.exec())

