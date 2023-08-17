# Copyright © https://steam.oxxostudio.tw

n = int(input())             # 輸入要產生的數字數量
arr = []                     # 建立一個空串列，記錄數字
for i in range(n):           # 使用 for 迴圈，重複指定的數字
    if i==0:                 # 如果 i 等於 0，a 為 0
        a = 0
    elif i==1:               # 如果 i 等於 1，a 為 1
        a = 1
        arr = [0, 1]         # 將串列設定為 [0, 1]
    else:                    # 如果 i 大於 1
        a = arr[0] + arr[1]  # a 等於串列的兩個數字相加
        del arr[0]           # 刪除串列的第一個項目
        arr.append(a)        # 將 a 加入串列成為第二個項目
    print(a, end=',')        # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181

