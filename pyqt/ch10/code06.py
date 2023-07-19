# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets     # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

label = QtWidgets.QLabel(Form)
label.setGeometry(10,10,200,200)

label.setText(f'''
    x: {Form.x()}
    y: {Form.y()}
    w: {Form.width()}
    h: {Form.height()}
    t: {Form.windowTitle()}
''')

Form.show()
sys.exit(app.exec())
