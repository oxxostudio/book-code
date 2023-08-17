# Copyright © https://steam.oxxostudio.tw

import os
import google.cloud.dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dialogflow_key.json'  # 金鑰 json
project_id = 'XXXX'         # dialogflow 的 project id
language = 'zh-TW'          # 語系
session_id = 'oxxostudio'   # 自訂義的 session id

def dialogflowFn(text):
    session_client = dialogflow.SessionsClient()                   # 使用 Token 和 dialogflow 建立連線
    session = session_client.session_path(project_id, session_id)  # 連接對應專案
    text_input = dialogflow.types.TextInput(text=text, language_code=language)  # 設定語系
    query_input = dialogflow.types.QueryInput(text=text_input)     # 根據語系取得輸入內容
    try:
        response = session_client.detect_intent(session=session, query_input=query_input) # 連線 Dialogflow 取得回應資料
        print("input:", response.query_result.query_text)
        print("intent:", response.query_result.intent.display_name)
        print("reply:", response.query_result.fulfillment_text)
        return response.query_result.fulfillment_text    # 回傳回應的文字
    except:
        return 'error'

def webhook(request):
    try:
        #req = request.get_json()
        text = request.args.get('text')
        return dialogflowFn(text)
    except:
        print(request.args)

