# Copyright © https://steam.oxxostudio.tw

a = 10                                # 要產生的金字塔層數
for i in range(1,a+1):                # 使用 for 迴圈，重複 1～10 ( a+1 ) 的數字
    print(' '*3*(a-i),end='')         # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    for j in range(1, i+1):           # 第二層 for 迴圈，重複不同層內的數字
        if j==1:                      # 如果是第一個數字
            print(j, end='')          # 單純印出數字即可 ( 後方不換行 )
        else:                         # 如果是第二個以後的數字
            print(f'{j:>3d}', end='') # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    for j in range(i-1, 0, -1):       # 剛剛的 for 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f'{j:>3d}', end='')     # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    print('')                         # 最後執行換行的 print

