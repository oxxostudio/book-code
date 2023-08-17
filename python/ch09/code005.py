# Copyright © https://steam.oxxostudio.tw

import threading
import time

def aa():
    lock.acquire()         # 鎖定
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)
        if i==2:
            lock.release()  # i 等於 2 時解除鎖定

def bb():
    lock.acquire()          # 鎖定
    i = 0
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)
    lock.release()

lock = threading.Lock()         # 建立 Lock
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

'''
A: 1
A: 2
B: 10
A: 3
B: 20
A: 4
B: 30
A: 5
B: 40
B: 50
'''
