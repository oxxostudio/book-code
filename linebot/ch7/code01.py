# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
# 載入 json 標準函式庫，處理回傳的資料格式
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi('你的 LINE Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        # 轉換內容為 json 格式
        json_data = json.loads(body)
        print(json_data)
    except:
        print('error')
    return 'OK'
if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()