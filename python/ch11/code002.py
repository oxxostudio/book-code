# Copyright © https://steam.oxxostudio.tw

a = input('請輸入兩個數字 ( 格式 a,b )：')
b = a.split(',')
b1 = int(b[0])
b2 = int(b[1])
print(f'{b1} + {b2} = {b1+b2}')
print(f'{b1} - {b2} = {b1-b2}')
print(f'{b1} x {b2} = {b1*b2}')
print(f'{b1} / {b2} = {round(b1/b2,3)}')    # 使用 round 四捨五入到小數點三位
print(f'{b2} + {b1} = {b2+b1}')
print(f'{b2} - {b1} = {b2-b1}')
print(f'{b2} x {b1} = {b2*b1}')
print(f'{b2} / {b1} = {round(b2/b1,3)}')

