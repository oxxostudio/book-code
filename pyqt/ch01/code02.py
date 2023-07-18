from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()          # 建立視窗元件
Form.setWindowTitle('oxxo.studio')  # 設定視窗標題
Form.resize(300, 200)               # 設定視窗尺寸

label = QtWidgets.QLabel(Form)      # 在 Form 裡加入標籤
label.setText('hello world')        # 設定標籤文字

Form.show()                         # 顯示視窗
sys.exit(app.exec())
