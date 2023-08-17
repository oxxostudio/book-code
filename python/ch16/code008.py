# Copyright © https://steam.oxxostudio.tw

import requests
# 建立 Proxy List
proxy_ips = ['80.93.213.213:3136',
'191.241.226.230:53281',
'207.47.68.58:21231',
'176.241.95.85:48700'
]
# 依序執行 get 方法
for ip in proxy_ips:
    try:
        result = requests.get('https://www.google.com', proxies={'http': 'ip', 'https': ip})
        print(result.text)
    except:
        print(f"{ip} invalid")

