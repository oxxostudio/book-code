# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.a = 0    # 設定 a 屬性為 0
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('0')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,100,30)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('增加數字')
        self.btn.setGeometry(50,60,100,30)
        self.btn.clicked.connect(self.showNum)  # 點擊時執行 showNum 方法

    # 注意不能使用 show 作為 class 內部方法的名稱
    def showNum(self):
        self.a = self.a + 1               # 每次執行讓 self.a 增加 1
        self.label.setText(str(self.a))   # 更新 QLabel 內容

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
