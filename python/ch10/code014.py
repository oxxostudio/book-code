# Copyright © https://steam.oxxostudio.tw

import time
n = 10
for i in range(n+1):
    print(f'\r倒數 {n-i} 秒', end='')
    time.sleep(1)
print('\r時間到', end='')

