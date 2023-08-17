# Copyright © https://steam.oxxostudio.tw

import requests
# 設定參數
params = {
    'name':'oxxo',
    'age':'18'
}
# 加入參數
web = requests.get('https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec', params=params)
print(web.text)

