# Copyright © https://steam.oxxostudio.tw

import requests
url = '你的氣象觀測資料 JSON 網址'
data = requests.get(url)
data_json = data.json()
location = data_json['cwbopendata']['location']
for i in location:
  name = i['locationName']                    # 測站地點
  city = i['parameter'][0]['parameterValue']  # 城市
  area = i['parameter'][2]['parameterValue']  # 行政區
  print(city, area, name)

