# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img = Image.new('RGBA', (360, 180))
font = ImageFont.truetype('NotoSansTC-Regular.otf', 40)
draw = ImageDraw.Draw(img)
draw.text((10,120), 'OXXO.STUDIO', fill=(255,255,255), font=font, stroke_width=2, stroke_fill='red')
draw.text(xy=(50,0), text='大家好\n哈哈', align='center', fill=(255,255,255), font=font, stroke_width=2, stroke_fill='blue')
img.save('ok.png')

video = VideoFileClip("baby_shark.mp4")         # 讀取影片
clip = video.resize((360,180)).subclip(10,12)   # 縮小影片尺寸，剪輯出 10～12 秒的片段
text_clip = ImageClip("ok.png", transparent=True).set_duration(2)   # 讀取圖片，將圖片變成長度兩秒的影片

output = CompositeVideoClip([clip, text_clip])  # 混合影片
output.write_videofile("output.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

print('ok')

