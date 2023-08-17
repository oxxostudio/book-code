# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup

url = 'https://www.iana.org/domains/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")

print(soup.select('#logo'))            # 搜尋 id 為 logo 的 tag 內容
print('\n----------\n')

print(soup.find_all('div',id="logo"))  # 搜尋所有 id 為 logo 的 div
print('\n----------\n')

divs = soup.find_all('div')            # 搜尋所有的 div
print(divs[1])                         # 取得搜尋到的第二個項目 ( 第一個為 divs[0] )
print('\n----------\n')

# 從搜尋到的項目裡，尋找父節點裡所有的 li
print(divs[1].find_parent().find_all('li'))
print('\n----------\n')

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他後方同層的所有 li
print(divs[1].find_parent().find_all('li')[2].find_next_siblings())
print('\n----------\n')

# 從搜尋到的項目裡，尋找父節點裡所有 li 的第三個項目，找到他前方同層的所有 li
print(divs[1].find_parent().find_all('li')[2].find_previous_siblings())

