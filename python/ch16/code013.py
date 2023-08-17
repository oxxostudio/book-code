# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = 'https://water.taiwanstat.com/'
web = requests.get(url)                        # 取得網頁內容
soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
title = soup.title                             # 取得 title
print(title)                                   # 印出 title ( 台灣水庫即時水情 )

