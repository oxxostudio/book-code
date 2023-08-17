# Copyright © https://steam.oxxostudio.tw

year = int(input('>'))             # 使用變數 year 紀錄使用者輸入的年份
if year%4 == 0:                    # 如果除以 4 能整除
    if year%100 == 0:              # 如果除以 100 能整除
        if year%400 == 0:          # 如果除以 400 能整除，就是閏年
            print(f'{year} 是閏年')
        else:
            print(f'{year} 是平年')
    else:
      print(f'{year} 是閏年')
else:
    print(f'{year} 是平年')

