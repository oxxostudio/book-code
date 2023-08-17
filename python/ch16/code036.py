# Copyright © https://steam.oxxostudio.tw

import requests

url = '一般天氣預報 - 今明 36 小時天氣預報 JSON 連結'
data = requests.get(url)   # 取得 JSON 檔案的內容為文字
data_json = data.json()    # 轉換成 JSON 格式
location = data_json['cwbopendata']['dataset']['location']   # 取出 location 的內容
for i in location:
    print(f'{i}')

