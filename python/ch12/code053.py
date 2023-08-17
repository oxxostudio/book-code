# Copyright © https://steam.oxxostudio.tw

import psutil

print(psutil.users())       # 登陸的使用者資訊
print(psutil.boot_time())   # 系統啟動時間
print(datetime.datetime.fromtimestamp(psutil.boot_time())) # 轉換成標準時間

