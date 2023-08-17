# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request

app = Flask(__name__)

@app.route("/",methods=['POST'])
def home():
    print(request.form)            # 使用 request.form
    return "<h1>hello world</h1>"

app.run()
