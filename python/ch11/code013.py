# Copyright © https://steam.oxxostudio.tw

a = range(2, 100)        # 產生 2～100 的串列
p = 0                    # 設定 p 從 0 開始 ( 從 a[p] 也就是第一個項目開始 )
def g():                 # 定義一個函式 g
    global p, a            # 設定 p 和 a 是全域變數
    if p<len(a):           # 如果 p 小於 a 的長度 ( 依序取值到 a 的最後一個項目 )
        a = [i for i in a if i==a[p] or i%a[p]>0]  # 重新設定 a 為移除倍數後的串列
        p = p + 1            # p 增加 1
        g()                  # 重新執行函式 g
g()                      # 執行函式 g
print(*a)                # 印出 a ( 使用 * 將串列打散印出 )

'''
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
'''

