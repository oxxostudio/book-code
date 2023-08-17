# Copyright © https://steam.oxxostudio.tw

import requests
import csv
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')   # 針對 Colab 改變路徑
csvfile = open('csv-aqi.csv', 'w')    # 建立空白並可寫入的 CSV 檔案
csv_write = csv.writer(csvfile)       # 設定 csv_write 為寫入

url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = requests.get(url)
data_json = data.json()
output = [['county','sitename','aqi','空氣品質']]    # 設定 output 變數為二維串列，第一筆資料為開頭
for i in data_json['records']:
    # 依序將取得的資料加入 output 中
    output.append([i['county'],i['sitename'],i['aqi'],i['status']])
print(output)
csv_write.writerows(output)   # 多行寫入 CSV

