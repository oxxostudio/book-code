# Copyright © https://steam.oxxostudio.tw

import requests

url = 'https://notify-api.line.me/api/notify'
token = '剛剛複製的權杖'
headers = {
    'Authorization': 'Bearer ' + token
}
data = {
    'message':'測試一下！',
    'imageThumbnail':'https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png',
    'imageFullsize':'https://steam.oxxostudio.tw/downlaod/python/line-notify-demo.png'
}
data = requests.post(url, headers=headers, data=data)

