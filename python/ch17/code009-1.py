# Copyright © https://steam.oxxostudio.tw

import requests
data = {'name': 'oxxo', 'age': '18'}
web = requests.post('http://127.0.0.1:5000/', data=data)   # 發送 POST 請求
print(web.text)
