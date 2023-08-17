# Copyright © https://steam.oxxostudio.tw

import threading
import time

def aa():
    event.wait()            # 等待事件被觸發
    event.clear()           # 觸發後將事件回歸原本狀態
    for i in range(1,6):
        print('A:',i)
        time.sleep(0.5)

def bb():
    for i in range(10,60,10):
        if i == 30:
            event.set()     # 觸發事件
        print('B:',i)
        time.sleep(0.5)

event = threading.Event()   # 註冊事件
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

'''
B: 10
B: 20
B: 30
A: 1
B: 40
A: 2
B: 50
A: 3
A: 4
A: 5
'''

