# Copyright © https://steam.oxxostudio.tw

import json
from linebot import LineBotApi, WebhookHandler
# 載入對應的函式庫
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

def linebot(request):
    try:
        body = request.get_data(as_text=True)
        # json 格式化收到的訊息
        json_data = json.loads(body)
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        # 取得 reply token
        tk = json_data['events'][0]['replyToken']
        # 取得 message 的類型
        tp = json_data['events'][0]['message']['type']
        if tp == 'text':
            # 如果是文字類型的訊息，取出文字並對應到 reply_msg 的函式
            msg = reply_msg(json_data['events'][0]['message']['text'])
            if msg[0] == 'text':
                # 如果要回傳的訊息是 text，使用 TextSendMessage 方法
                line_bot_api.reply_message(tk,TextSendMessage(text=msg[1]))
            if msg[0] == 'location':
                # 如果要回傳的訊息是 location，使用 LocationSendMessage 方法
                line_bot_api.reply_message(tk,LocationSendMessage(title=msg[1]['title'],
                                                                address=msg[1]['address'],
                                                                latitude=msg[1]['latitude'],
                                                                longitude=msg[1]['longitude']))
            if msg[0] == 'image':
                # 如果要回傳的訊息是 image，使用 ImageSendMessage 方法
                line_bot_api.reply_message(tk,ImageSendMessage(original_content_url=msg[1],
                                                                preview_image_url=msg[1]))
        if tp == 'sticker':
            # 如果收到的訊息是表情貼圖
            stickerId = json_data['events'][0]['message']['stickerId'] # 取得 stickerId
            packageId = json_data['events'][0]['message']['packageId'] # 取得 packageId
            # 使用 StickerSendMessage 方法回傳同樣的表情貼圖
            line_bot_api.reply_message(tk,StickerSendMessage(sticker_id=stickerId, package_id=packageId))
        if tp == 'location':
            # 如果是收到的訊息是地點資訊
            line_bot_api.reply_message(tk,TextSendMessage(text='好地點！'))
        if tp == 'image':
            # 如果是收到的訊息是圖片
            line_bot_api.reply_message(tk,TextSendMessage(text='好圖給讚！'))
        if tp == 'audio':
            # 如果是收到的訊息是聲音
            line_bot_api.reply_message(tk,TextSendMessage(text='聲音讚喔～'))
        if tp == 'video':
            # 如果是收到的訊息是影片
            line_bot_api.reply_message(tk,TextSendMessage(text='影片內容真是不錯！'))
    except:
        print('error', body)
    return 'OK'
# 定義回覆訊息的函式
def reply_msg(text):
    # 客製化回覆文字
    msg_dict = {
        'hi':'Hi! 你好呀～',
        'hello':'Hello World!!!!',
        '你好':'你好呦～',
        'help':'有什麼要幫忙的嗎？'
    }
    # 如果出現特定地點，提供地點資訊
    local_dict = {
        '總統府':{
            'title':'總統府',
            'address':'100台北市中正區重慶南路一段122號',
            'latitude':'25.040319874750914',
            'longitude':'121.51162883484746'
        }
    }
    # 如果出現特定圖片文字，提供圖片網址
    img_dict = {
        '皮卡丘':'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png',
        '傑尼龜':'https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png'
    }
    # 預設回覆的文字就是收到的訊息
    reply_msg_content = ['text',text]
    if text in msg_dict:
        reply_msg_content = ['text',msg_dict[text.lower()]]
    if text in local_dict:
        reply_msg_content = ['location',local_dict[text.lower()]]
    if text in img_dict:
        reply_msg_content = ['image',img_dict[text.lower()]]
    return reply_msg_content