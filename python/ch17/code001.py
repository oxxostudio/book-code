# Copyright © https://steam.oxxostudio.tw

from flask import Flask   # 載入 Flask

app = Flask(__name__)     # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式

@app.route("/")           # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def home():               # 發出請求後會執行 home() 的函式
    return "<h1>hello world</h1>"   # 執行函式後會回傳特定的網頁內容

app.run()                 # 執行

