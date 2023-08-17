# Copyright © https://steam.oxxostudio.tw

c = int(input('輸入 1 ( 公分 ) 或 2 ( 英吋 )：'))
length = int(input('輸入長度數值：'))

print('|cm   |m    |ich  |foot |yd   |')        # 印出說明
print('|-----|-----|-----|-----|-----|')        # 印出分隔線

if c == 1:
    print('|',end='')                              # 印出表格左側的框線
    print(f'{str(length):<5.5s}', end='|')
    print(f'{str(length*0.01):<5.5s}', end='|')
    print(f'{str(length*0.394):<5.5s}', end='|')
    print(f'{str(length*0.03281):<5.5s}', end='|')
    print(f'{str(length*0.01094):<5.5s}', end='|')
else:
    print('|',end='')
    print(f'{str(length*2.54):<5.5s}', end='|')
    print(f'{str(length*0.0254):<5.5s}', end='|')
    print(f'{str(length):<5.5s}', end='|')
    print(f'{str(length/12):<5.5s}', end='|')
    print(f'{str(length/36):<5.5s}', end='|')

