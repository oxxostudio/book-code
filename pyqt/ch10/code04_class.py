# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets            # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.setMouseTracking(True)
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(20,20,100,30)

    def keyPressEvent(self, event):
        keycode = event.key()             # 取得該按鍵的 keycode
        self.label.setText(str(keycode))  # QLabel 印出 keycode

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())

