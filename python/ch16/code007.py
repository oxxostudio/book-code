# Copyright © https://steam.oxxostudio.tw

import requests
cookies = {'over18':'1'}
# 加入 Cookies 資訊
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies=cookies)
print(web.text)

