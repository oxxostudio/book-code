# Copyright © https://steam.oxxostudio.tw

import requests

headers = {'Authorization':'Bearer 你的 Access Token'}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/你的圖文選單 ID', headers=headers)

print(req.text)
