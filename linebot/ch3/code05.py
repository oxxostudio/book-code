# Copyright © https://steam.oxxostudio.tw

import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

def linebot(request):
    try:
        access_token = '你的 LINE Channel access token'
        secret = '你的 LINE Channel secret'
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        msg = json_data['events'][0]['message']['text']
        tk = json_data['events'][0]['replyToken']
        line_bot_api.reply_message(tk,TextSendMessage(msg))
        print(msg, tk)
    except:
        print(request.args)
    return 'OK'
