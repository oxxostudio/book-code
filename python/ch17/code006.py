# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route("/<msg>")           # 加入 <msg> 讀取網址
def ok(msg):                   # 加入參數
    return f"<h1>{msg}</h1>"   # 使用變數

app.run()

