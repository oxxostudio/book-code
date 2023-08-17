# Copyright © https://steam.oxxostudio.tw

import requests
web = requests.get('https://water.taiwanstat.com/')  # 使用 get 方法
print(web.text)    # 讀取並印出 text 屬性

