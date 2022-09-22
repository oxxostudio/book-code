# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler

# 載入 TextSendMessage 模組
from linebot.models import TextSendMessage
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        # 取得 reply token
        tk = json_data['events'][0]['replyToken']
        # 取得使用者發送的訊息
        msg = json_data['events'][0]['message']['text']
        # 設定回傳同樣的訊息
        text_message = TextSendMessage(text=msg)
        # 回傳訊息
        line_bot_api.reply_message(tk,text_message)
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()