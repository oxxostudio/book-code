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
        self.label.setText('A')
        self.label.setStyleSheet('font-size:20px;')
        self.label.setGeometry(50,30,100,30)

        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('A')
        self.btn1.setGeometry(50,60,50,30)
        self.btn1.clicked.connect(lambda:self.showText('A'))  # 使用 lambda 函式

        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setText('B')
        self.btn2.setGeometry(110,60,50,30)
        self.btn2.clicked.connect(lambda:self.showText('B'))  # 使用 lambda 函式

    # 注意不能使用 show 作為 class 內部方法的名稱
    def showText(self, text):
        self.label.setText(text)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())
