# Copyright © https://steam.oxxostudio.tw

import requests
url = '你的應用程式網址'
name = '工作表1'
row = 2
web = requests.get(f'{url}?name={name}&row={row}')
print(web.json())
name = '工作表2'
web = requests.get(f'{url}?name={name}')
print(web.json())

