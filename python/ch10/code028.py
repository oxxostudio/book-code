# Copyright © https://steam.oxxostudio.tw

import datetime
import time

while True:
    now = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'\r{now}', end = '')     # 前方加上 \r
    time.sleep(1)

