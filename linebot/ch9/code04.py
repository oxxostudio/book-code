# Copyright © https://steam.oxxostudio.tw

import requests

url = 'https://notify-api.line.me/api/notify'
# 自己申請的 LINE Notify 權杖
token = '你的 LINE Notify 權杖'
# POST 使用的 headers
headers = {
    'Authorization': 'Bearer ' + token
}
# POST 使用的 data
data = {
    'message':'從雷達回波看看會不會下雨～',
    'imageThumbnail':'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png',
    'imageFullsize':'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png'
}
data = requests.post(url, headers=headers, data=data)