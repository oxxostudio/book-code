# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request, render_template    # 載入 render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name')
    return render_template('test.html', name=name)  # 使用網頁樣板，並傳入參數

app.run()

