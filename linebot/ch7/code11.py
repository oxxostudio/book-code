# Copyright © https://steam.oxxostudio.tw

import requests

headers = {"Authorization":"Bearer 你的 access token", "Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/圖文選單 id', headers=headers)

print(req.text)