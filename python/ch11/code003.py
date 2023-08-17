# Copyright © https://steam.oxxostudio.tw

a = input('請輸入數字 ( 格式 a,b,c... )：')   # 新增變數 a，內容是使用者輸入的多個數字，數字以逗號分隔
b = a.split(',')      # 新增變數 b，內容使用 split 根據逗號將數字拆開為串列
output = 0            # 設定 output 從 0 開始
for i in b:           # 使用 for 迴圈，依序取出 b 串列的每個項目
    output += int(i)  # 將 output 的數值加上每個項目 ( 使用 int 將項目轉換成數字 )

print(f'數字總和為：{output}')

