# Copyright © https://steam.oxxostudio.tw

import time

def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)

def bb():
    i = 0
    while i<100:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)

def cc():
    i = 0
    while i<500:
        i = i + 100
        time.sleep(0.5)
        print('C:', i)

a = threading.Thread(target=aa)
b = threading.Thread(target=bb)
c = threading.Thread(target=cc)

a.start()
b.start()
a.join()   # 加入等待 aa() 完成的方法
c.start()  # 當 aa() 完成後，就會開始執行 cc()

'''
A: 1
B: 10
A: 2
B: 20
A: 3
B: 30
A: 4
B: 40
A: 5
B: 50
C: 100 <--- A 結束就開始
B: 60
C: 200
B: 70
C: 300
B: 80
C: 400
B: 90
C: 500
B: 100
'''

