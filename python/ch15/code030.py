# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

def time2sec(t):
    arr = t.split(' --> ')
    s1 = arr[0].split(',')
    s2 = arr[1].split(',')
    start = int(s1[0].split(':')[0])*3600 + int(s1[0].split(':')[1])*60 + int(s1[0].split(':')[2]) + float(s1[1])*0.001
    end = int(s2[0].split(':')[0])*3600 + int(s2[0].split(':')[1])*60 + int(s2[0].split(':')[2]) + float(s2[1])*0.001
    return [start, end]

f = open('oxxostudio.srt','r')
srt = f.read()
f.close()
srt_list = srt.split('\n')
#print(text_list)
sec = 1
text = 2
srt_list = [[0,0]]
text_list = ['']
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            sec_list.append([sec_list[-1][1],time2sec(srt_list[i])[0]])
            text_list.append('')
        sec_list.append(time2sec(srt_list[i]))
    if i == text:
        text = text + 4
        text_list.append(srt_list[i])

print(sec_list)
print(text_list)

img_empty = Image.new('RGBA', (480, 240))                 # 產生 RGBA 空圖片
font = ImageFont.truetype('NotoSansTC-Regular.otf', 20)   # 設定文字字體和大小
video = VideoFileClip("baby_shark.mp4").resize((480,240)) # 讀取影片，改變尺寸
video_duration = float(video.duration)                    # 讀取影片總長度
output_list = []                                          # 記錄最後要組合的影片片段

# 如果字幕最後的時間小於總長度
if sec_list[-1][1] != video_duration:
    sec_list.append([sec_list[-1][1],video_duration])     # 添加時間到時間串列
    text_list.append('')                                  # 添加空字串到文字串列

# 建立文字字卡函式
def text_clip(text, name):
    img = img_empty.copy()      # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    text_width = 21*len(text)   # 在 480x240 文字大小 20 狀態下，一個中文字長度約 21px
    draw.text(((480-text_width)/2,10), text, fill=(255,255,255), font=font, stroke_width=2, stroke_fill='black')
    img.save(name)              # 儲存

# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0],t[1])                  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(t[1]-t[0])  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)                 # 添加到影片片段裡

# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i], 'srt.png')
    text_in_video(sec_list[i], 'srt.png')

output = concatenate_videoclips(output_list)      # 合併所有影片片段
output.write_videofile("output.mp4",temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")
print('ok')

