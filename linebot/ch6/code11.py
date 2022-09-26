# Copyright © https://steam.oxxostudio.tw

import requests
import json
headers = {'Authorization':'Bearer 你的 access token','Content-Type':'application/json'}
body = {
    "richMenuAliasId":"aaa",
    "richMenuId":"圖文選單 id"
}
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
print(req.text)