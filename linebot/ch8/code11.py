# Copyright © https://steam.oxxostudio.tw

import os
import google.cloud.dialogflow_v2 as dialogflow

import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 剛剛下載的金鑰 json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dialogflow_key.json'
project_id = 'XXXXX'        # dialogflow 的 project id
language = 'zh-TW'          # 語系
session_id = 'oxxostudio'   # 自訂義的 session id

def dialogflowFn(text):
    # 使用 Token 和 dialogflow 建立連線
    session_client = dialogflow.SessionsClient()
    # 連接對應專案
    session = session_client.session_path(project_id, session_id)
    # 設定語系
    text_input = dialogflow.types.TextInput(text=text, language_code=language)
    # 根據語系取得輸入內容
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        # 連線 Dialogflow 取得回應資料
        response = session_client.detect_intent(session=session, query_input=query_input)
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        # 回傳回應的文字
        return response.query_result.fulfillment_text
    except:
        return 'error'

def webhook(request):
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
        if type=='text':
            # 取得 LINE 收到的文字訊息
            msg = json_data['events'][0]['message']['text']
            # 印出內容
            print(msg)
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