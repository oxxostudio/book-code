# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img_empty = Image.new('RGBA', (360, 180))                  # 產生 RGBA 空圖片
font = ImageFont.truetype('NotoSansTC-Regular.otf', 24)    # 設定文字字體和大小
video = VideoFileClip("oxxostudio.mp4").resize((360,180))  # 讀取影片，改變尺寸
output_list = []      # 記錄最後要組合的影片片段

# 建立文字字卡函式
def text_clip(xy, text, name):
    img = img_empty.copy()      # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    draw.text(xy, text, fill=(255,255,255), font=font, stroke_width=2, stroke_fill='black')
    img.save(name)              # 儲存

# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0],t[1])    # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(t[1]-t[0])  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)   # 添加到影片片段裡

# 文字串列，包含座標和內容
text_list = [
    [(100,140),'你到底要怎樣？'],
    [(90,140),'給我 CDPRO2 呀！'],
    [(60,140),'但是 CDPRO2 過時啦！']
]

# 影片串列，包含要切取的時間片段
video_list = [
    [13,16],
    [21,24],
    [38,41]
]

# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i][0], text_list[i][1], f'text_{i}.png')

# 使用 for 迴圈，合併字卡和影片
for i in range(len(video_list)):
    text_in_video(video_list[i], f'text_{i}.png')

output = concatenate_videoclips(output_list)      # 合併所有影片片段
output.write_gif("output.gif", fps=6, colors=32)  # 轉換成 gif 動畫
print('ok')

