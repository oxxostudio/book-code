# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(320, 240)
        self.ui()

    def ui(self):
        self.btn = QtWidgets.QPushButton(self)  # 建立按鈕
        self.btn.setText('按鈕')                # 設定按鈕文字
        self.btn.setGeometry(50,50,100,50)      # 設定位置和長寬
        # 設定樣式
        self.btn.setStyleSheet('''
            background:#ff0;
            color:#f00;
            font-size:20px;
            border:2px solid #000;
        ''')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
