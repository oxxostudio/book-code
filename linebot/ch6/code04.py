# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler
# 需要額外載入對應的函示庫
from linebot.models import MessageAction, TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn
line_bot_api = LineBotApi('你的 Channel access token')
line_bot_api.push_message('你的 user ID', TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png',
                action=MessageAction(
                    label='皮卡丘',
                    text='皮卡丘'
                )
            ),
            ImageCarouselColumn(
                image_url='https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png',
                action=MessageAction(
                    label='傑尼龜',
                    text='傑尼龜'
                )
            )
        ]
    )
))