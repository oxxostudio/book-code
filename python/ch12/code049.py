# Copyright © https://steam.oxxostudio.tw

import psutil

print(psutil.cpu_count())               # CPU 邏輯數量
print(psutil.cpu_count(logical=False))  # 實際物理 CPU 數量
print(psutil.cpu_percent(interval=0.5, percpu=True)) # CPU 使用率
                                                     # interval：每隔多少秒更新一次
                                                     # percpu：查看所有 CPU 使用率
print(psutil.cpu_freq())                # CPU 使用頻率

