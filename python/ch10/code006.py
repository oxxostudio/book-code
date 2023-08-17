# Copyright © https://steam.oxxostudio.tw

year = int(input('>'))
text = '平年'                # 新增變數 text 預設平年
if year%4 == 0:
    text = '閏年'            # 如果除以 4 能整除，將 text 改為閏年
if year%100 == 0:
    text = '平年'            # 如果除以 100 能整除，將 text 改為平年
if year%400 == 0:
    text = '閏年'            # 如果除以 400 能整除，將 text 改為閏年
print(f'{year} 是{text}')

