# Copyright © https://steam.oxxostudio.tw

import psutil

print(psutil.disk_partitions())             # 所有硬碟資訊
print(psutil.disk_usage('硬碟 device 名稱')) # 指定硬碟資訊

