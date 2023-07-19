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
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('按鈕')
        self.btn.setGeometry(50,50,100,50)
        self.btn.setStyleSheet('''
            QPushButton {
                font-size:20px;
                color: #f00;
                background: #ff0;
                border: 2px solid #000;
            }
            QPushButton:disabled {
                color:#fff;
                background:#ccc;
                border: 2px solid #aaa;
            }
        ''')
        self.btn.setDisabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
