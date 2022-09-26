# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler
# 需要額外載入對應的函示庫
from linebot.models import MessageAction, TemplateSendMessage, ConfirmTemplate
line_bot_api = LineBotApi('你的 Channel access token')
line_bot_api.push_message('你的 user ID', TemplateSendMessage(
    alt_text='ConfirmTemplate',
    template=ConfirmTemplate(
            text='你好嗎？',
            actions=[
                MessageAction(
                    label='好喔',
                    text='好喔'
                ),
                MessageAction(
                    label='好喔',
                    text='不好喔'
                )
            ]
        )
))