# Copyright © https://steam.oxxostudio.tw

a = 15
b = a*2+1
for i in range(1,b,4):     # 改成 4 個一數，金字塔每一層就會增加 2，高度也會減半
    move = round((b-i)/2)-1
    print(f' '*move, end='')
    print('*'*i)

