# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# 建立要抓取的股票網址清單
stock_urls = [
  'https://tw.stock.yahoo.com/quote/2330',
  'https://tw.stock.yahoo.com/quote/0050',
  'https://tw.stock.yahoo.com/quote/2317',
  'https://tw.stock.yahoo.com/quote/6547'
]

# 將剛剛的抓取程式變成「函式」
def getStock(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    title = soup.find('h1')
    a = soup.select('.Fz(32px)')[0]
    b = soup.select('.Fz(20px)')[0]
    s = ''
    try:
        if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C($c-trend-down)')[0]:
            s = '-'
    except:
        try:
            if soup.select('#main-0-QuoteHeader-Proxy')[0].select('.C($c-trend-up)')[0]:
                s = '+'
        except:
            state = ''
    print(f'{title.get_text()} : {a.get_text()} ( {s}{b.get_text()} )')

executor = ThreadPoolExecutor()         # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(getStock, stock_urls)  # 開始同時爬取股價

