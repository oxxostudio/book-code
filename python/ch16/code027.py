# Copyright © https://steam.oxxostudio.tw

import requests
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})  # 加入 Cookies 資訊
print(web.text)

