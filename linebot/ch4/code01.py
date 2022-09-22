# Copyright © https://steam.oxxostudio.tw

# 如果是本機環境不用 flask_ngrok
from flask_ngrok import run_with_ngrok

from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    # 讀取資料 json_data
    body = request.get_data(as_text=True)
    # 轉換成 json 格式 ( 字典格式 )
    json_data = json.loads(body)
    print(json_data)
    return 'OK'

if __name__ == "__main__":
    # 如果是本機環境不用 run_with_ngrok(app)
    run_with_ngrok(app)
    app.run()