# Copyright © https://steam.oxxostudio.tw

import requests

url = 'https://notify-api.line.me/api/notify'
token = '剛剛複製的權杖'
headers = {
    'Authorization': 'Bearer ' + token
}
data = {
    'message':'測試一下！',
    'stickerPackageId':'446',
    'stickerId':'1989'
}
data = requests.post(url, headers=headers, data=data)
