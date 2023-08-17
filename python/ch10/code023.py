# Copyright © https://steam.oxxostudio.tw

import random
a = random.randint(1,99)                         # 產生 1～99 的隨機整數
b = int(input('輸入 1～99 的數字：'))               # 讓使用者輸入數字，使用 int 轉換成數字
while a!=b:                                      # 使用 while 迴圈，如果 a 不等於 b，就不斷繼續
    if b < a:
        b = int(input('數字太小囉！再試一次吧：'))   # 如果 b<a，提示數字太小
    elif b > a:
        b = int(input('數字太大囉！再試一次吧：'))   # 如果 b>a，提示數字太大
print('答對囉！')                                 # 如果 b=a 會停止 while 迴圈，顯示正確答案

