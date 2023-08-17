# Copyright © https://steam.oxxostudio.tw

import math       # import math 標準函式模組

text = input('輸入文字：')                # 讓使用者輸入文字
length = len(text)                      # 取得輸入的文字長度
center = math.floor(length/2)           # 取出中間值
if length%2 == 0:                       # 如果除以 2 餘數為 0，表示偶數
    print(f'{text[center-1:center+1]}')   # 取出中間兩個字元
else:
    print(f'{text[center]}')              # 如果是奇數，取出中間一個字元

