# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
print(soup.find_all('a'))                     # 找出所有 a tag
print(soup.find_all('a', string='Domains'))   # 找出內容字串為 Domains 的 a tag
print(soup('a', limit=2))                     # 找出前兩個 a tag
