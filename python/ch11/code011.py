# Copyright © https://steam.oxxostudio.tw

a = b = int(input('請輸入一個正整數：')) # 新增 a 和 b 變數，等於使用者輸入的數字
output = ''                           # 新增 output 變數，作為輸出的文字
while True:                           # 使用 while 迴圈
    for i in range(2,(a+1)):          # 使用 for 迴圈
        if i==b:                      # 如果 i 等於 b，表示是質數，跳出 for 迴圈
            break
        if a%i==0:                    # 如果可以被 i 整除，表示不是質數
            output += f'{i}'          # 設定 output 輸出的內容
            a = int(a/i)              # 重新將 a 設定為商
            break                     # 跳出 for 迴圈
    if a==1 or a==b:                  # 如果商等於 1 或是質數，跳出 while 迴圈
        break
    else:
        output += '*'                 # 否則在 output 後方加上 * 號，繼續 while 迴圈
if b == a and b!= 1:
    print(f'{b} 是質數')               # while 迴圈結束後，如果 a 等於 b，印出質數的文字
elif b == 1:
    print(f'{b} 不是質數，也不能質因數分解')  # 如果輸入的是 1 或 2
else:
    print(f'{b}={output}')            # 否則印出質因數分解的結果

