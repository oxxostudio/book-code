# Copyright © https://steam.oxxostudio.tw

import requests
import json
headers = {'Authorization':'Bearer 你的 access token','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 640},    # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'bbb',                             # 選單名稱
    'chatBarText': 'b',                        # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
          'bounds': {'x': 0, 'y': 0, 'width': 1250, 'height': 640},           # 選單位置與大小
          'action': {'type': 'uri', 'uri': 'https://line.me/R/nv/location/'}  # 點擊後開啟地圖定位，傳送位置資訊
        },
        {
          'bounds': {'x': 1251, 'y': 0, 'width':625, 'height': 640},     # 選單位置與大小
          'action': {'type': 'message', 'text':'雷達回波圖'}               # 點擊後傳送文字
        },
        {
          'bounds': {'x': 1879, 'y': 0, 'width':625, 'height': 640},     # 選單位置與大小
          'action': {'type': 'message', 'text':'地震資訊'}               # 點擊後傳送文字
        }
    ]
  }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)