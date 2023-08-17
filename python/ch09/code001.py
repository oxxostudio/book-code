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
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)

aa()    # 先執行 aa()
bb()    # aa() 結束後才會執行 bb()

'''
A: 1
A: 2
A: 3
A: 4
A: 5
B: 10
B: 20
B: 30
B: 40
B: 50
'''

