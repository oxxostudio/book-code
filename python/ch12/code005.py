# Copyright © https://steam.oxxostudio.tw

import pyautogui
import requests
import time

# 定義截圖的函式
def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('./test.png')

    t = time.time()           # 取得到目前為止的秒數
    t1 = time.localtime(t)    # 將秒數轉換為 struct_time 格式的時間
    now = time.strftime('%Y/%m/%d %H:%M:%S',t1)  # 輸出為特定格式的文字
    sendLineNotify(now)       # 執行發送 LINE Notify 的函式，發送的訊息為時間

# 定義發送 LINE Notify 的函式
def sendLineNotify(msg):
    url = 'https://notify-api.line.me/api/notify'
    token = '你的權杖'
    headers = {
      'Authorization': 'Bearer ' + token
    }
    data = {
      'message':msg
    }
    image = open('./test.png', 'rb')
    imageFile = {'imageFile' : image}
    data = requests.post(url, headers=headers, data=data, files=imageFile)

# 使用for 迴圈，每隔五秒截圖發送一次
for i in range(5):
    screenshot()
    time.sleep(5)


