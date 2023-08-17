# Copyright © https://steam.oxxostudio.tw

import requests
ip = requests.get('https://api.ipify.org').text

print(ip)

