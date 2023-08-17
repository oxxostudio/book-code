# Copyright © https://steam.oxxostudio.tw

a = input('請輸入兩個數字 ( 格式 a,b )：')  # 新增變數 a，內容是使用者輸入的兩個數字，數字以逗號分隔
b = a.split(',')                  # 新增變數 b，內容使用 split 根據逗號將數字拆開為串列
b1 = int(b[0])                    # 使用 int 將第一個值轉換為「數字」
b2 = int(b[1])                    # 使用 int 將第二個值轉換為「數字」
print(f'{b1} + {b2} = {b1+b2}')   # 印出四則運算的結果
print(f'{b1} - {b2} = {b1-b2}')
print(f'{b1} x {b2} = {b1*b2}')
print(f'{b1} / {b2} = {b1/b2}')

