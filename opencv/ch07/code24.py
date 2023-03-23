from PIL import Image,ImageSequence
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture('video.mov')   # 開啟影片
source = []                           # 建立 source 空串列，記錄影格內容
frame = 0                             # frame 從 0 開始

print('loading...')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    if frame%30 == 0:                                # 每 30 格取一格
        img = cv2.resize(img, (400,300))             # 改變尺寸，加快處理效率
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 修改顏色為 RGBA
        source.append(img)                           # 記錄該圖片
    frame = frame + 1
    if cv2.waitKey(1) == ord('q'):
        break                                        # 按下 q 鍵停止
cap.release()

print('start...')
for i in range(len(source)):
    for x in range(400):
        for y in range(300):
            r = source[i][y,x,0]   # 該像素的紅色數值
            g = source[i][y,x,1]   # 該像素的綠色數值
            b = source[i][y,x,2]   # 該像素的藍色數值
            if r>35 and r<100 and g>110 and g<200 and b>60 and b< 130:
                source[i][y,x,3] = 0    # 如果在顏色範圍內，將透明度設為 0

print('export single frame to gif...')
n = 0
for i in source:
    img = Image.fromarray(i)
    img.save(f'temp/gif{n}.gif')
    n = n + 1

print('loading gifs...')
output = []
for i in range(n):
    img = Image.open(f'temp/gif{i}.gif')
    img = img.convert("RGBA")
    output.append(img)

output[0].save("test2.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)
print('ok...')

cv2.destroyAllWindows()
