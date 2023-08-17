# Copyright © https://steam.oxxostudio.tw

def fib(n):                         # 建立函式 fib，帶有參數 n
    if n > 1:                       # 如果 n 大於 1
        return fib(n-1) + fib(n-2)  # 使用遞迴
    return n
for i in range(20):                 # 產生 20 個數字
    print(fib(i), end = ',')        # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181



