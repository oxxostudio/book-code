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
        # 設定 QCheckBox
        style = '''
            QCheckBox {
                color: #00f;
            }
            QCheckBox:hover {
                color: #f00;
            }
            QCheckBox:checked {
                color: #fff;
                background: #000;
            }
        '''

        self.cb_a = QtWidgets.QCheckBox(self)
        self.cb_a.move(30, 60)
        self.cb_a.setText('A')
        self.cb_a.setStyleSheet(style)    # 套用 style

        self.cb_b = QtWidgets.QCheckBox(self)
        self.cb_b.move(80, 60)
        self.cb_b.setText('B')
        self.cb_b.setStyleSheet(style)    # 套用 style

        self.cb_c = QtWidgets.QCheckBox(self)
        self.cb_c.move(130, 60)
        self.cb_c.setText('C')
        self.cb_c.setStyleSheet(style)    # 套用 style

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
