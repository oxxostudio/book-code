# Copyright © https://steam.oxxostudio.tw

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor   # 加入 concurrent.futures 內建函式庫

web = requests.get('https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html', cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
imgs = soup.find_all('img')
name = 0
img_urls = []                          # 根據爬取的資料，建立一個圖片名稱與網址的空串列
for i in imgs:                         # 修改 for 迴圈內容
    img_urls.append([i['src'], name])    # 將圖片網址與編號加入串列中
    name = name + 1                      # 編號增加 1

def download(url):                     # 編輯下載函式
    print(url)                           # 印出網址
    jpg = requests.get(url[0])           # 使用 requests.get 取得圖片資訊
    f = open(f'download/test_{url[1]}.jpg', 'wb')    # 將圖片開啟為二進位格式 ( 請自行修改存取路徑 )
    f.write(jpg.content)                 # 存取圖片
    f.close()

executor = ThreadPoolExecutor()          # 建立非同步的多執行緒的啟動器
with ThreadPoolExecutor() as executor:
    executor.map(download, img_urls)     # 同時下載圖片

