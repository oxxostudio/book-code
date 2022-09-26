# Copyright © https://steam.oxxostudio.tw

import requests
url = '你取得的地震資訊 JSON 網址'
data = requests.get(url)
data_json = data.json()
eq = data_json['records']['earthquake']    # 轉換成 json 格式
for i in eq:
    loc = i['earthquakeInfo']['epiCenter']['location']        # 地震地點
    val = i['earthquakeInfo']['magnitude']['magnitudeValue']  # 芮氏規模
    dep = i['earthquakeInfo']['depth']['value']               # 地震深度
    eq_time = i['earthquakeInfo']['originTime']               # 地震時間
    print(f'地震發生於{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}')