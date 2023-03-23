from PIL import Image,ImageSequence
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

output = []                       # 建立輸出的空串列

cap = cv2.VideoCapture(0)         # 從攝影鏡頭取得影像
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img, (450,240))    # 調整影片大小

    # 加上黑色區塊
    cv2.rectangle(img,(10,10),(200,42),(0,0,0),-1)

    # 加上文字
    text = 'oxxo.studio'
    org = (15,35)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255,255,255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)

    gif = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 轉換顏色
    gif = Image.fromarray(gif)                    # 轉換成 PIL 格式
    gif = gif.convert('RGB')                      # 轉換顏色
    output.append(gif)                            # 添加到 output

    cv2.imshow('oxxostudio', img)
    if cv2.waitKey(250) == ord('q'):
        break
cap.release()
# 儲存為 gif 動畫
output[0].save("test2.gif", save_all=True, append_images=output[1:], duration=250, loop=0, disposal=2)
cv2.destroyAllWindows()
