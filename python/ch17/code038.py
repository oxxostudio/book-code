# Copyright © https://steam.oxxostudio.tw

import requests

url = 'https://notify-api.line.me/api/notify'
token = '剛剛複製的權杖'
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
data = {
    'message':'測試一下！'     # 設定要發送的訊息
}
data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法

