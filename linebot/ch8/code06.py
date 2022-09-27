# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()    # 轉換成 dict 格式
    print(req)
    reText = req['queryResult']['fulfillmentText']   # 取得回覆文字
    print(reText)
    return {
          "fulfillmentText": f'{reText} ( webhook )',
          "source": "webhookdata"
      }

# Colab 使用，本機環境請刪除
run_with_ngrok(app)


app.run()
