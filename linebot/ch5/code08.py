# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

def pushmsg(request):
  line_bot_api = LineBotApi('你的 access token')
  try:
    msg = request.args.get('msg')
    if msg == '1':
      line_bot_api.push_message('你的 user ID', TextSendMessage(text='hello'))
    elif msg == '2':
      line_bot_api.push_message('你的 user ID', StickerSendMessage(package_id=1, sticker_id=2))
    elif msg == '3':
      imgurl = 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'
      line_bot_api.push_message('你的 user ID', ImageSendMessage(original_content_url=imgurl, preview_image_url=imgurl))
    elif msg == '4':
      line_bot_api.push_message('你的 user ID', LocationSendMessage(title='總統府',
                                                address='100台北市中正區重慶南路一段122號',
                                                latitude='25.040319874750914',
                                                longitude='121.51162883484746'))
    else:
      msg = 'ok'
    return msg
  except:
    print('error')