# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = 'https://water.taiwanstat.com/'
web = requests.get(url)
# soup = BeautifulSoup(web.text, "html.parser")  # 使用 html.parser 解析器
soup = BeautifulSoup(web.text, "html5lib")       # 使用 html5lib 解析器
title = soup.title
print(title)

