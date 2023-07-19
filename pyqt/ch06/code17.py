# Copyright © https://steam.oxxostudio.tw

from PyQt6 import QtWidgets   # 將 PyQt6 換成 PyQt5 就能改用 PyQt5
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

bar = QtWidgets.QProgressBar(Form) # 建立進度條
bar.move(20,20)
bar.setRange(0, 100)    # 進度條範圍
bar.setValue(50)        # 進度條預設值

Form.show()
sys.exit(app.exec())
