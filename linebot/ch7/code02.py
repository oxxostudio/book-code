# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 載入 json 標準函式庫，處理回傳的資料格式
import requests, json, time

app = Flask(__name__)

access_token = '你的 LINE Channel access token'
channel_secret = '你的 LINE Channel secret'

@app.route("/", methods=['POST'])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        # 轉換內容為 json 格式
        json_data = json.loads(body)
        # 取得回傳訊息的 Token ( reply message 使用 )
        reply_token = json_data['events'][0]['replyToken']
        # 取得使用者 ID ( push message 使用 )
        user_id = json_data['events'][0]['source']['userId']
        print(json_data)
        # 如果傳送的是 message
        if 'message' in json_data['events'][0]:
            # 如果 message 的類型是文字 text
            if json_data['events'][0]['message']['type'] == 'text':
                # 取出文字
                text = json_data['events'][0]['message']['text']
                # 如果是雷達回波圖相關的文字
                if text == '雷達回波圖' or text == '雷達回波':
                    # 傳送雷達回波圖 ( 加上時間戳記 )
                    reply_image(f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}', reply_token, access_token)
                else:
                    # 如果是一般文字，直接回覆同樣的文字 
                    reply_message(text, reply_token, access_token)
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    # Colab 使用，本機環境請刪除
    run_with_ngrok(app)
    app.run()

# LINE 回傳圖片函式
def reply_image(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}
    body = {
    'replyToken':rk,
    'messages':[{
          'type': 'image',
          'originalContentUrl': msg,
          'previewImageUrl': msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)