# Copyright © https://steam.oxxostudio.tw

import psutil

for prcs in psutil.process_iter():
    print(prcs.name)           # 印出所有正在執行的應用程式 ( 從中觀察 pid )

p = psutil.Process(pid=3987)   # 讀取特定應用程式
print(p.name())                # 應用程式名稱
print(p.exe())                 # 應用程式所在路徑
print(p.cwd())                 # 應用程式執行路徑
print(p.status())              # 應用程式狀態
print(p.username())            # 執行應用程式的使用者
print(p.cpu_times())           # 應用程式的 CPU 使用時間
print(p.memory_info())         # 應用程式的 RAM 使用資訊

