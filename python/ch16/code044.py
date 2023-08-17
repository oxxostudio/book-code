# Copyright © https://steam.oxxostudio.tw

import requests
url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url)    # 取得網頁內容
web.encoding='utf-8'       # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼

from bs4 import BeautifulSoup
soup = BeautifulSoup(web.text, "html.parser")                    # 轉換成標籤樹
td = soup.select('.container-fluid')[0].select('.etw-tbiggest')  # 取出中獎號碼的位置
ns = td[0].getText()  # 特別獎
n1 = td[1].getText()  # 特獎
# 頭獎，因為存入串列會出現 /n 換行符，使用 [-8:] 取出最後八碼
n2 = [td[2].getText()[-8:], td[3].getText()[-8:], td[4].getText()[-8:]] 

while True:
    try:
        # 對獎程式
        num = input('輸入你的發票號碼：')
        if num == ns: print('對中 1000 萬元！')
        if num == n1: print('對中 200 萬元！')
        for i in n2:
            if num == i:
                print('對中 20 萬元！')
                break
            if num[-7:] == i[-7:]:
                print('對中 4 萬元！')
                break
            if num[-6:] == i[-6:]:
                print('對中 1 萬元！')
                break
            if num[-5:] == i[-5:]:
                print('對中 4000 元！')
                break
            if num[-4:] == i[-4:]:
                print('對中 1000 元！')
                break
            if num[-3:] == i[-3:]:
                print('對中 200 元！')
                break
    except: break

