# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
import sys
import zipfile

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(400, 300)
        self.ui()

    def ui(self):
        self.fileList = []

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('選擇檔案')
        self.btn1.setGeometry(20,5,80,35)
        self.btn1.clicked.connect(self.open)

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('壓縮存檔')
        self.btn2.setGeometry(300,5,80,35)
        self.btn2.clicked.connect(self.zipFile)

        self.input = QtWidgets.QTextEdit(self)
        self.input.setGeometry(20,40,360,240)
        self.input.setLineWrapMode(self.input.LineWrapMode.NoWrap)

    def open(self):
        filePath , filterType = QtWidgets.QFileDialog.getOpenFileNames()
        print(filePath , filterType)
        for i in filePath:
            if i not in self.fileList:
                self.fileList.append(i)
        output = '\n'.join(self.fileList)
        self.input.setText(output)

    def zipFile(self):
        zf = zipfile.ZipFile('test.zip', mode='w')
        for i in self.fileList:
            zf.write(i)
        zf.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

