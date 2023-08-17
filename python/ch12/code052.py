# Copyright © https://steam.oxxostudio.tw

import psutil

print(psutil.net_io_counters())  # 網路封包
print(psutil.net_if_addrs())     # 網路卡的組態資訊, 包括 IP 地址、Mac地址、子網掩碼、廣播地址等等
print(psutil.net_connections())  # 目前機器的網路連線

