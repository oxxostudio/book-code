# Copyright © https://steam.oxxostudio.tw

import random
a = []                           # 建立空串列
while len(a)<6:                  # 使用 while 迴圈，直到串列的長度等於 6 就停止
    b = random.randint(1, 49)    # 取出 1～49 得隨機整數
    if b not in a:               # 判斷如果 a 裡面沒有 b
        a.append(b)              # 將 b 放入 a
print(a)                         # [34, 18, 31, 11, 47, 46]

