# Copyright © https://steam.oxxostudio.tw

import requests, json, time
def webhook(request):
    try:
        req = request.get_json()
        reText = req['queryResult']['fulfillmentText']
        intent = req['queryResult']['intent']['displayName']
        replytoken = req['originalDetectIntentRequest']['payload']['data']['replyToken']
        token = '你的 LINE BOT Access Token'
        img = f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}'
        if intent=='radar':
            headers = {'Authorization':'Bearer ' + token,'Content-Type':'application/json'}
            body = {
                'replyToken':replytoken,
                'messages':[{
                        'type': 'image',
                        'originalContentUrl': img,
                        'previewImageUrl': img
                    }]
                }
            result = requests.request('POST', 'https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(body).encode('utf-8'))
            print(result.text)
            return {
                "source": "webhookdata"
            }
        else:
            return {
                "fulfillmentText": f'{reText} ( webhook )'
            }
    except:
        print(request.args)