# Copyright © https://steam.oxxostudio.tw

import requests
web = requests.post('http://127.0.0.1:5000/')  # 使用 post 方法
print(web.text)    # 讀取並印出 text 屬性

