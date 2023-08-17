# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
print(soup.find('a').get_text())   # 輸出第一個 a tag 的內容
print(soup.find('a')['href'])      # 輸出第一個 a tag 的 href 屬性內容

