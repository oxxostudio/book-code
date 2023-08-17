# Copyright © https://steam.oxxostudio.tw

import datetime
import time

def timezone(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h))       # 取得時區
    return datetime.datetime.now(tz=GMT).strftime('%H:%M:%S')  # 回傳該時區的時間

# 六個時區的名稱與時差
local = {'倫敦':1,
        '台灣':8,
        '日本':9,
        '紐約':-4,
        '洛杉磯':-7,
        '紐西蘭':12 }

while True:
    print('\r',end='')   # 開始時將游標移到開頭
    # 讀取 local 的 key
    for i in local:
        now = timezone(local[i])   # 根據 key 的 value 取得時間
        print(f'{i}>{timezone(local[i])}  ', end='')
    time.sleep(1)
    # 倫敦>08:43:09  台灣>15:43:09  日本>16:43:09  紐約>03:43:09  洛杉磯>00:43:09  紐西蘭>19:43:09 

