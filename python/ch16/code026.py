# Copyright © https://steam.oxxostudio.tw

import requests
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html')
print(web.text)

