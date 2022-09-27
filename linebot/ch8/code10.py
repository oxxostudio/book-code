# Copyright © https://steam.oxxostudio.tw

import os
import google.cloud.dialogflow_v2 as dialogflow
from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dialogflow_key.json' # 金鑰 json
project_id = 'XXXX'         # dialogflow project id
language = 'zh-TW'          # 語系
session_id = 'oxxostudio'   # 自訂 session id

# dialogflow 處理自然語言
def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language)
    query_input = dialogflow.types.QueryInput(text=text_input)
    print(query_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text
    except:
        return 'error'

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    # 取得收到的訊息內容
    body = request.get_data(as_text=True)
    try:
        # json 格式化訊息內容
        json_data = json.loads(body)
        access_token = 'Access Token'
        secret = 'Channel Secret'
        # 確認 token 是否正確
        line_bot_api = LineBotApi(access_token)
        # 確認 secret 是否正確
        handler = WebhookHandler(secret)
        # 加入回傳的 headers
        signature = request.headers['X-Line-Signature']
        # 綁定訊息回傳的相關資訊
        handler.handle(body, signature)
         # 取得回傳訊息的 Token
        tk = json_data['events'][0]['replyToken']
        # 取得 LINe 收到的訊息類型
        type = json_data['events'][0]['message']['type']
        # 取得 LINE 收到的文字訊息
        if type=='text':
            msg = json_data['events'][0]['message']['text']
            # 印出內容
            print(msg)
            # dialogflow 處理後回傳文字
            reply = dialogflowFn(msg)
        else:
            reply = '你傳的不是文字呦～'
        print(reply)
        # 回傳訊息
        line_bot_api.reply_message(tk,TextSendMessage(reply))
    except:
        print(body)
    # 驗證 Webhook 使用，不能省略
    return 'OK'

if __name__ == "__main__":
    app.run()