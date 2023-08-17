# Copyright © https://steam.oxxostudio.tw

c = int(input('輸入 1 ( 攝氏 ) 或 2 ( 華氏 )：'))   # 使用變數 c 記錄攝氏還是華氏
t = int(input('輸入溫度數值：'))                    # 使用變數 t 記錄要轉換的數值

if c == 1:
    print(f'攝氏 {t} 度等於華氏 {9/5*t+32} 度')       # 套用攝氏轉華氏公式
else:
    print(f'華氏 {t} 度等於攝氏 {(t-32)*5/9} 度')     # 套用華氏轉攝氏公式

