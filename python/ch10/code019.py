# Copyright © https://steam.oxxostudio.tw

a = 15                     # 新增變數 a，設定金字塔有幾層
for i in range(1,a+1):     # 使用 for 迴圈，重複指定的層數
    print(' ' * (a-i) + '*' * (2*i-1))
    # ' ' * (a-i) 表示星星數越少，前面空白越多
    # '*' * (2*i-1) 串接後方星星的數量

