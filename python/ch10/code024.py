# Copyright © https://steam.oxxostudio.tw

import random
a = random.randint(1,99)
b = int(input('輸入 1～99 的數字：'))
while True:
    if b < a:
        b = int(input('數字太小囉！再試一次吧：'))
    elif b > a:
        b = int(input('數字太大囉！再試一次吧：'))
    else:
        print('答對囉！')
        break;

