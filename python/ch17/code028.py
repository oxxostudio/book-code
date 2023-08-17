# Copyright © https://steam.oxxostudio.tw

import requests

url = '部署的網址'

params = {
    'name':'工作表1',
    'top':'true',
    'data':'[123,456,789]'
}

web = requests.get(url=url, params=params)

