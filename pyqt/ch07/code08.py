# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def open():
    filename , filetype = QtWidgets.QFileDialog.getOpenFileNames(directory='test', filter='TXT (*.txt)')
    print(filename, filetype)

btn = QtWidgets.QPushButton(Form)
btn.move(20, 20)
btn.setText('開啟檔案')
btn.clicked.connect(open)

Form.show()
sys.exit(app.exec())

