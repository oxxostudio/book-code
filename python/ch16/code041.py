# Copyright © https://steam.oxxostudio.tw

import requests

url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'   # 牌告匯率 CSV 網址
rate = requests.get(url)   # 爬取網址內容
rate.encoding = 'utf-8'    # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = rate.text             # 以文字模式讀取內容
rts = rt.split('\n')       # 使用「換行」將內容拆分成串列
for i in rts:              # 讀取串列的每個項目
    try:                             # 使用 try 避開最後一行的空白行
        a = i.split(',')             # 每個項目用逗號拆分成子串列
        print(a[0] + ': ' + a[12])   # 取出第一個 ( 0 ) 和第十三個項目 ( 12 )
    except:
      break

