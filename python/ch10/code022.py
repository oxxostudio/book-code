# Copyright © https://steam.oxxostudio.tw

a = 10                                # 要產生的金字塔層數
b = 1                                 # 提供 while 迴圈停止的依據
while b<=a:                           # 如果 b <= a 就讓 while 迴圈繼續
    n = 1                             # 設定從 1 開始
    print(' '*3*(a-b),end='')         # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    while n<=b:                       # 第二層 while 迴圈，如果 n <= b 就讓 while 迴圈繼續
        if n==1:                      # 如果是第一個數字
            print(n, end='')          # 單純印出數字即可 ( 後方不換行 )
        else:                         # 如果是第二個以後的數字
            print(f'{n:>3d}', end='') # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n + 1                     # 將 n 增加 1
    while n>2:                        # 剛剛的 while 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f'{n-2:>3d}', end='')   # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n - 1                     # 將 n 減少 1
    print('')                         # 最後執行換行的 print
    b = b + 1                         # 將 b 增加 1

