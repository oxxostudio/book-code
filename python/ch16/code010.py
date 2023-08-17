# Copyright © https://steam.oxxostudio.tw

import requests
web = requests.get('https://water.taiwanstat.com/')  # 使用 get 方法
web.encoding='utf-8'       # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
print(web.text)

