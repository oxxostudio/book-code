# Copyright © https://steam.oxxostudio.tw

from flask_ngrok import run_with_ngrok
from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        # json 格式化訊息內容
        json_data = json.loads(body)
        access_token = '你的 LINE Channel access token'
        secret = '你的 LINE Channel secret'
        # 確認 token 是否正確
        line_bot_api = LineBotApi(access_token)
        # 確認 secret 是否正確
        handler = WebhookHandler(secret)
        # 加入回傳的 headers
        signature = request.headers['X-Line-Signature']
        # 綁定訊息回傳的相關資訊
        handler.handle(body, signature)
        # 取得 LINE 收到的文字訊息
        msg = json_data['events'][0]['message']['text']
        # 取得回傳訊息的 Token
        tk = json_data['events'][0]['replyToken']
        # 回傳訊息
        line_bot_api.reply_message(tk,TextSendMessage(msg))
        # 印出內容
        print(msg, tk)
    except:
        # 如果發生錯誤，印出收到的內容
        print(body)
    # 驗證 Webhook 使用，不能省略
    return 'OK'
if __name__ == "__main__":
  # 串連 ngrok 服務
  run_with_ngrok(app)
  app.run()