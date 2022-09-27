# Copyright © https://steam.oxxostudio.tw

def webhook(request):
    try:
        req = request.get_json()
        reText = req['queryResult']['fulfillmentText']
        return {
              "fulfillmentText": f'{reText} ( webhook )',
              "source": "webhookdata"
          }
    except:
        print(request.args)