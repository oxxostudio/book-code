# Copyright © https://steam.oxxostudio.tw

import requests, json
headers = {'Authorization':'Bearer 你的 access token','Content-Type':'application/json'}

body = {
    'size': {'width': 2500, 'height': 1200},   # 設定尺寸
    'selected': 'true',                        # 預設是否顯示
    'name': 'ccc',                             # 選單名稱 ( 別名 Alias Id )
    'chatBarText': '選單 C',                    # 選單在 LINE 顯示的標題
    'areas':[                                  # 選單內容
        {
          'bounds': {'x': 0, 'y': 0, 'width': 830, 'height': 280},
          'action': {'type': 'richmenuswitch', 'richMenuAliasId': 'aaa', 'data':'change-to-aaa'} # 按鈕 A 使用 richmenuswitch
        },
        {
          'bounds': {'x': 835, 'y': 0, 'width':830, 'height': 640},
          'action': {'type': 'richmenuswitch', 'richMenuAliasId': 'bbb', 'data':'change-to-ccc'} # 按鈕 B 使用 richmenuswitch
        },
        {
          'bounds': {'x': 1670, 'y': 0, 'width':830, 'height': 640},
          'action': {'type': 'postback', 'data':'no-data'}          # 按鈕 C 使用 postback
        }
    ]
  }
req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                      headers=headers,data=json.dumps(body).encode('utf-8'))
print(req.text)