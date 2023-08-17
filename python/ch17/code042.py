# Copyright © https://steam.oxxostudio.tw

from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)     # 連結 ngrok

@app.route("/")
def home():
    return "<h1>hello world</h1>"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    print(req)
    reText = req['queryResult']['fulfillmentText']
    print(reText)
    return {
          "fulfillmentText": f'{reText} ( webhook )',
          "source": "webhookdata"
      }

app.run()

