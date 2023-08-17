# Copyright © https://steam.oxxostudio.tw

import random
a = set()                       # 建立空集合
while len(a)<6:                 # 使用 while 迴圈，直到集合的長度等於 6 就停止
    b = random.randint(1, 49)   # 取出 1～49 得隨機整數
    a.add(b)                    # 將隨機數加入集合
print(a)                        # {34, 41, 48, 49, 19, 30}

