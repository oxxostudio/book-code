# Copyright © https://steam.oxxostudio.tw

import requests, time

url = 'https://notify-api.line.me/api/notify'
token = '你的 LINE Notify 權杖'
headers = {
    'Authorization': 'Bearer ' + token
}
radar_img = 'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png'
time_now = str(time.time_ns())   # 取得目前時間
data = {
    'message':'從雷達回波看看會不會下雨～',
    'imageThumbnail':radar_img + '?' + time_now,   # 加上時間參數
    'imageFullsize':radar_img + '?' + time_now     # 加上時間參數
}
data = requests.post(url, headers=headers, data=data)
