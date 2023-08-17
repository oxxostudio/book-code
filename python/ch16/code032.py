# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

web = requests.get('https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html', cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = 0
for i in imgs:
    print(i['src'])
    jpg = requests.get(i['src'])
    f = open(f'content/drive/MyDrive/Colab Notebooks/download/test_{name}.jpg', 'wb')
    f.write(jpg.content)
    f.close()
    name = name + 1

