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
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.move(20, 20)
        self.btn1.setText('開啟檔案')
        self.btn1.clicked.connect(self.openFiles)     # 點擊執行開啟檔案函式

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.move(120, 20)
        self.btn2.setText('開啟資料夾')
        self.btn2.clicked.connect(self.openFolder)    # 點擊執行開啟資料夾函式

    def openFiles(self):
        filePath, filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選取多個檔案
        print(filePath, filterType )

    def openFolder(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()        # 選取特定資料夾
        print(folderPath)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

