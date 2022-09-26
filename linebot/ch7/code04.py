# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time

app = Flask(__name__)

access_token = '你的 LINE Channel access token'
channel_secret = '你的 LINE Channel secret'

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    try:
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(channel_secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        json_data = json.loads(body)
        reply_token = json_data['events'][0]['replyToken']
        user_id = json_data['events'][0]['source']['userId']
        print(json_data)
        if 'message' in json_data['events'][0]:
            if json_data['events'][0]['message']['type'] == 'text':
                text = json_data['events'][0]['message']['text']
                if text == '雷達回波圖' or text == '雷達回波':
                    reply_image(f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}', reply_token, access_token)
                # 如果是地震相關的文字
                elif text == '地震資訊' or text == '地震':
                    # 爬取地震資訊
                    msg = earth_quake()
                    # 傳送地震資訊 ( 用 push 方法，因為 reply 只能用一次 )
                    push_message(msg[0], user_id, access_token)
                    # 傳送地震圖片 ( 用 reply 方法 )
                    reply_image(msg[1], reply_token, access_token)
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

# 地震資訊函式
def earth_quake():
    # 預設回傳的訊息
    msg = ['找不到地震資訊','https://example.com/demo.jpg']
    try:
        code = '你的氣象資料授權碼'
        url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0016-001?Authorization={code}'
        # 爬取地震資訊網址
        e_data = requests.get(url)
        # json 格式化訊息內容
        e_data_json = e_data.json()
        # 取出地震資訊
        eq = e_data_json['records']['earthquake']
        for i in eq:
            loc = i['earthquakeInfo']['epiCenter']['location']       # 地震地點
            val = i['earthquakeInfo']['magnitude']['magnitudeValue'] # 地震規模
            dep = i['earthquakeInfo']['depth']['value']              # 地震深度
            eq_time = i['earthquakeInfo']['originTime']              # 地震時間
            img = i['reportImageURI']                                # 地震圖
            msg = [f'{loc}，芮氏規模 {val} 級，深度 {dep} 公里，發生時間 {eq_time}。', img]
            break     # 取出第一筆資料後就 break
        return msg    # 回傳 msg
    except:
        return msg    # 如果取資料有發生錯誤，直接回傳 msg

# LINE push 訊息函式
def push_message(msg, uid, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}   
    body = {
    'to':uid,
    'messages':[{
            "type": "text",
            "text": msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/push', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)

# LINE 回傳訊息函式
def reply_message(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}','Content-Type':'application/json'}
    body = {
    'replyToken':rk,
    'messages':[{
            "type": "text",
            "text": msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)

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