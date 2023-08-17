# Copyright © https://steam.oxxostudio.tw

num_table = [
    [1000,'M'],
    [900,'CM'],
    [500,'D'],
    [400,'CD'],
    [100,'C'],
    [90,'XC'],
    [50,'L'],
    [40,'XL'],
    [10,'X'],
    [9,'IX'],
    [5,'V'],
    [4,'IV'],
    [1,'I']]                          # 建立對照表
num = int(input())                    # 將輸入的文字轉換成數字
output = ''                           # 設定輸出的 output 字串
for i in num_table:                   # 依序判斷對照表中每個數字
    a = divmod(num, i[0])             # 取得商 ( a[0] ) 和餘數 ( a[1] )
    if a[0]!=0:                       # 如果 a[0] 不為 0
        num = a[1]                    # 取得餘數繼續往下除
        output = output + i[1]*a[0]   # 組合字串
print(output)

