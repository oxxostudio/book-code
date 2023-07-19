# Copyright © https://steam.oxxostudio.tw

# 將 PyQt6 換成 PyQt5 就能改用 PyQt5
from PyQt6 import QtWidgets
import pyaudio
import sys, wave, threading, random

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oxxo.studio')
        self.resize(400, 300)
        self.setUpdatesEnabled(True)
        self.chunk = 1024                     # 記錄聲音的樣本區塊大小
        self.sample_format = pyaudio.paInt16  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
        self.channels = 2                     # 聲道數量
        self.fs = 44100                       # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
        self.seconds = 5                      # 錄音秒數
        self.ui()

    def ui(self):
        self.label = QtWidgets.QLabel(self)   # 在 Form 中加入一個 QLabel
        self.label.setGeometry(10, 10, 200, 30)
        self.label.setText('準備開始錄音')

        self.btn1 = QtWidgets.QPushButton(self)   # 在 Form 中加入一個 QPushButton
        self.btn1.setGeometry(10,40,80,30)
        self.btn1.setText('錄音')                 # 按鈕文字
        self.btn1.clicked.connect(self.start)

        self.btn2 = QtWidgets.QPushButton(self)   # 在 Form 中加入一個 QPushButton
        self.btn2.setGeometry(100,40,80,30)
        self.btn2.setText('停止')                 # 按鈕文字
        self.btn2.clicked.connect(self.stop)

    # 開始錄音
    def start(self):
        self.btn1.setDisabled(True)
        self.btn2.setDisabled(False)
        self.label.setText('錄音中....')
        event.set()      # 觸發錄音開始事件

    # 停止錄音
    def stop(self):
        self.btn1.setDisabled(False)
        self.btn2.setDisabled(True)
        self.label.setText('停止錄音')
        self.run = False       # 設定 run 為 False 停止錄音迴圈
        self.name, self.ok = QtWidgets.QInputDialog().getText(Form, '$', '存檔的檔名？')
        print(self.name, self.ok)
        if self.name == '':
            self.name = str(random.random()*10).replace('.','')  # 如果沒有檔名，使用 random 產生
        event2.set()      # 觸發錄音停止事件


    def recording(self):
        while True:
            event.wait()            # 等待事件被觸發
            event.clear()           # 觸發後將事件回歸原本狀態
            self.run = True              # 設定 run 為 True 表示開始錄音
            print('開始錄音...')
            p = pyaudio.PyAudio()   # 建立 pyaudio 物件
            stream = p.open(format=self.sample_format, channels=self.channels, rate=self.fs, frames_per_buffer=self.chunk, input=True)
            frames = [] 
            while self.run:
                data = stream.read(self.chunk)
                frames.append(data)          # 將聲音記錄到串列中
            print('停止錄音')
            stream.stop_stream()             # 停止錄音
            stream.close()                   # 關閉串流
            p.terminate()
            event2.wait()                    # 等待事件被觸發
            event2.clear()                   # 觸發後將事件回歸原本狀態
            # 如果存檔按下確定，表示要儲存
            if self.ok == True:
                wf = wave.open(f'{self.name}.wav', 'wb')   # 開啟聲音記錄檔
                wf.setnchannels(self.channels)             # 設定聲道
                wf.setsampwidth(p.get_sample_size(self.sample_format))  # 設定格式
                wf.setframerate(self.fs)                   # 設定取樣頻率
                wf.writeframes(b''.join(frames))      # 存檔
                wf.close()
            else:
                pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()

    event = threading.Event()   # 註冊錄音事件
    event2 = threading.Event()  # 註冊停止錄音事件
    record = threading.Thread(target=Form.recording)     # 將錄音的部分放入 threading 裡執行
    record.start()
    Form.show()
    sys.exit(app.exec())

