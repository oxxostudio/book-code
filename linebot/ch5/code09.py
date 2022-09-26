# Copyright © https://steam.oxxostudio.tw

import requests, json

# 設定 request 的 headers，注意前方要有 Bearer
headers = {'Authorization':'Bearer 你的 access token','Content-Type':'application/json'}

# 設定 request 的 body，必須包含 replyToken 和 messages
body = {
    'replyToken':replyToken,
    'messages':[{
            'type': 'text',
            'text': 'hello'
        }]
}

# 向指定網址用 POST 方法發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,data=json.dumps(body).encode('utf-8'))
print(req.text)
