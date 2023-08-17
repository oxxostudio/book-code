# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request   # 載入了 request

app = Flask(__name__)

@app.route("/")
def home():
    print(request.args)            # 使用 request.args
    return "<h1>hello world</h1>"

app.run()
