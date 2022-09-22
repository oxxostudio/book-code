# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
# 載入 TextSendMessage 和 LocationSendMessage 模組
from linebot.models import TextSendMessage, LocationSendMessage
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
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        # 取得對應的地址，如果沒有取得，會是 False
        location_dect = reply_location(msg)
        if location_dect:
            # 如果有地點資訊，回傳地點
            location_message = LocationSendMessage(title=location_dect['title'],
                                                  address=location_dect['address'],
                                                  latitude=location_dect['latitude'],
                                                  longitude=location_dect['longitude'])
            line_bot_api.reply_message(tk,location_message)
        else:
            # 如果是 False，回傳文字
            text_message = TextSendMessage(text='找不到相關地點')
            line_bot_api.reply_message(tk,text_message)
    except:
        print('error')
    return 'OK'
# 建立回覆地點的函式
def reply_location(text):
    # 建立地點與文字對應的字典
    location = {
        '101':{
            'title':'台北 101',
            'address':'110台北市信義區信義路五段7號',
            'latitude':'25.034095712145003',
            'longitude':'121.56489941996108'
        },
        '總統府':{
            'title':'總統府',
            'address':'100台北市中正區重慶南路一段122號',
            'latitude':'25.040319874750914',
            'longitude':'121.51162883484746'
        }
    }
    if text in location:
      return location[text]
    else:
      # 如果找不到對應的地點，回傳 False
      return False

if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()