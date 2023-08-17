# Copyright © https://steam.oxxostudio.tw

import time
from concurrent.futures import ThreadPoolExecutor

a = True               # 定義 a 為 True

def run():
    global a           # 定義 a 是全域變數
    while a:           # 如果 a 為 True
        print(123)     # 不斷顯示 123
        time.sleep(1)  # 每隔一秒

def keyin():
    global a           # 定義 a 是全域變數
    if input() == 'a':
        a = False      # 如果輸入的是 a，就讓 a 為 False，停止 run 函式中的迴圈

executor = ThreadPoolExecutor()
e1 = executor.submit(run)
e2 = executor.submit(keyin)
executor.shutdown()

