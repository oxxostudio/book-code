# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html', cookies={'over18':'1'})    # 傳送 Cookies 資訊後，抓取頁面內容
soup = BeautifulSoup(web.text, "html.parser")   # 使用 BeautifulSoup 取得網頁結構
imgs = soup.find_all('img')    # 取得所有 img tag 的內容
for i in imgs:
  print(i['src'])              # 印出 src 的屬性

