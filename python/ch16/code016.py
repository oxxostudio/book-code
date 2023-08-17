# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

print(soup.find_all('a'))    # 等同於下方的 soup('a')
print(soup('a'))             # 等同於上方的 find_all('a')

