# Copyright © https://steam.oxxostudio.tw

import os

hostname = 'google.com'
response = os.system('ping -c 3 -i 1 ' + hostname)
print(response)

response = os.popen(f'ping -c 3 -i 1 {hostname}').read()
print(response)

