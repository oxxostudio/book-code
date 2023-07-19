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
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(30, 30, 100, 20)

        self.rb_a = QtWidgets.QRadioButton(self)
        self.rb_a.setGeometry(30, 60, 100, 20)
        self.rb_a.setText('A')

        self.rb_b = QtWidgets.QRadioButton(self)
        self.rb_b.setGeometry(150, 60, 100, 20)
        self.rb_b.setText('B')

        self.group = QtWidgets.QButtonGroup(self)
        self.group.addButton(self.rb_a, 1)               # 添加 QRadioButton A，ID 設定為 1
        self.group.addButton(self.rb_b, 2)               # 添加 QRadioButton B，ID 設定為 2
        self.group.buttonClicked.connect(self.showId)      # 綁定點擊事件

    def showId(self):
        self.label.setText(str(self.group.checkedId()))   # 設定 label 文字為按鈕群組中勾選按鈕的 ID

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
