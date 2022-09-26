# Copyright © https://steam.oxxostudio.tw

# Colab 使用，本機環境請刪除
from flask_ngrok import run_with_ngrok

from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests, json, time, statistics  # import statistics 函式庫

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
            # 如果 message 的類型是地圖 location
            if json_data['events'][0]['message']['type'] == 'location':
                # 取出地址資訊，並將「台」換成「臺」  
                address = json_data['events'][0]['message']['address'].replace('台','臺')
                print(address)
                # 回覆爬取到的相關氣象資訊
                reply_message(f'{address}\n\n{current_weather(address)}', reply_token, access_token)
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

# 目前天氣函式
def current_weather(address):
    # 定義好待會要用的變數
    city_list, area_list, area_list2 = {}, {}, {}
    # 預設回傳訊息
    msg = '找不到氣象資訊。'

    # 定義取得資料的函式
    def get_data(url):
        # 爬取目前天氣網址的資料
        w_data = requests.get(url)
        # json 格式化訊息內容
        w_data_json = w_data.json()
        # 取出對應地點的內容
        location = w_data_json['cwbopendata']['location']  
        for i in location:
            name = i['locationName']                       # 測站地點
            city = i['parameter'][0]['parameterValue']     # 縣市名稱
            area = i['parameter'][2]['parameterValue']     # 鄉鎮行政區
            temp = check_data(i['weatherElement'][3]['elementValue']['value'])                       # 氣溫
            humd = check_data(round(float(i['weatherElement'][4]['elementValue']['value'] )*100 ,1)) # 相對濕度
            r24 = check_data(i['weatherElement'][6]['elementValue']['value'])                        # 累積雨量
            if area not in area_list:
                # 以鄉鎮區域為 key，儲存需要的資訊
                area_list[area] = {'temp':temp, 'humd':humd, 'r24':r24}
            if city not in city_list:
                # 以主要縣市名稱為 key，準備紀錄裡面所有鄉鎮的數值
                city_list[city] = {'temp':[], 'humd':[], 'r24':[]}
            city_list[city]['temp'].append(temp)   # 記錄主要縣市裡鄉鎮區域的溫度 ( 串列格式 )
            city_list[city]['humd'].append(humd)   # 記錄主要縣市裡鄉鎮區域的濕度 ( 串列格式 )
            city_list[city]['r24'].append(r24)     # 記錄主要縣市裡鄉鎮區域的雨量 ( 串列格式 )

    # 定義如果數值小於 0，回傳 False 的函式
    def check_data(e):
        return False if float(e)<0 else float(e)

    # 定義產生回傳訊息的函式
    def msg_content(loc, msg):
        a = msg
        for i in loc:
            if i in address: # 如果地址裡存在 key 的名稱
                temp = f"氣溫 {loc[i]['temp']} 度，" if loc[i]['temp'] != False else ''
                humd = f"相對濕度 {loc[i]['humd']}%，" if loc[i]['humd'] != False else ''
                r24 = f"累積雨量 {loc[i]['r24']}mm" if loc[i]['r24'] != False else ''
                description = f'{temp}{humd}{r24}'.strip('，')
                a = f'{description}。' # 取出 key 的內容作為回傳訊息使用
                break
        return a

    try:
        # 因為目前天氣有兩組網址，兩組都爬取
        code = '你的氣象資料授權碼'
        get_data(f'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0001-001?Authorization={code}&downloadType=WEB&format=JSON')
        get_data(f'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0003-001?Authorization={code}&downloadType=WEB&format=JSON')

        for i in city_list:
            if i not in area_list2: 
                # 將主要縣市裡的數值平均後，以主要縣市名稱為 key，再度儲存一次，如果找不到鄉鎮區域，就使用平均數值
                area_list2[i] = {'temp':round(statistics.mean(city_list[i]['temp']),1),
                                'humd':round(statistics.mean(city_list[i]['humd']),1),
                                'r24':round(statistics.mean(city_list[i]['r24']),1)
                                }
        msg = msg_content(area_list2, msg)  # 將訊息改為「大縣市」
        msg = msg_content(area_list, msg)   # 將訊息改為「鄉鎮區域」
        return msg    # 回傳 msg
    except:
        return msg    # 如果取資料有發生錯誤，直接回傳 msg