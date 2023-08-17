# Copyright © https://steam.oxxostudio.tw

table = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}  # 轉換對照表
roman = [i for i in input()]             # 將輸入的羅馬數字變成串列
r = roman[::-1]                          # 反轉串列
output = table[r[0]]                     # 讓 output 先等於第一個數字
for i in range(1, len(r)):               # 從第二個數字開始依序取到最後一個數字
    if table[r[i]] < table[r[i-1]]:      # 如果後面數字比較小
        output = output - table[r[i]]    # 讓 output 減去後面的數字
    else:
        output = output + table[r[i]]    # 如果後面數字比較大，讓 output 加上後面的數字
print(output)

# 輸入 IVMVIIMVVMVM 就會得到 3994
