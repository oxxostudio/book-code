# Copyright © https://steam.oxxostudio.tw

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route("/<path:msg>")     # 加入 path: 轉換成「路徑」的類型
def ok(msg):
    return f"<h1>{msg}</h1>"

app.run()

