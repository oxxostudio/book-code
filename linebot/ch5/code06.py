# Copyright © https://steam.oxxostudio.tw

# Colab 才需要，本機環境請刪除
from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage

app = Flask(__name__)

@app.route("/")
def home():
  line_bot_api = LineBotApi('你的 access token')
  try:
    # 取得網址的 msg 參數
    msg = request.args.get('msg')
    if msg != None:
      # 如果有 msg 參數，觸發 LINE Message API 的 push_message 方法
      line_bot_api.push_message('你的 User ID', TextSendMessage(text=msg))
      return msg
    else:
      return 'OK'
  except:
    print('error')

if __name__ == "__main__":
    # Colab 才需要，本機環境請刪除
    run_with_ngrok(app)
    app.run()