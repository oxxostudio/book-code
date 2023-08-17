# Copyright © https://steam.oxxostudio.tw

num = input('輸入你的發票號碼：')
ns = '05701942'                         # 特別獎
n1 = '97718570'                         # 特獎
n2 = ['88400675','73475574','53038222'] # 頭獎
if num == ns: print('對中 1000 萬元！')   # 對中特別獎
if num == n1: print('對中 200 萬元！')    # 對中特獎
# 頭獎判斷
for i in n2:
    if num == i:
        print('對中 20 萬元！')   # 對中頭獎
        break
    if num[-7:] == i[-7:]:
        print('對中 4 萬元！')    # 末七碼相同
        break
    if num[-6:] == i[-6:]:
        print('對中 1 萬元！')    # 末六碼相同
        break
    if num[-5:] == i[-5:]:
        print('對中 4000 元！')   # 末五碼相同
        break
    if num[-4:] == i[-4:]:
        print('對中 1000 元！')   # 末四碼相同
        break
    if num[-3:] == i[-3:]:
        print('對中 200 元！')    # 末三碼相同
        break

