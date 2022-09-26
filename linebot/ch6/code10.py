# Copyright © https://steam.oxxostudio.tw

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi('你的 Access Token')

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用

# 開啟對應的圖片
with open('line-rich-menu-switch-demo-a.jpg', 'rb') as f:
    line_bot_api.set_rich_menu_image('你的圖文選單 ID', 'image/jpeg', f)
