from PIL import Image,ImageSequence
# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

gif = Image.open('dot.gif')

img_list = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')
    opencv_img = np.array(frame, dtype=np.uint8)
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)

    # 在圖形中間繪製黑色方塊
    cv2.rectangle(opencv_img,(100,120),(300,180),(0,0,0),-1)

    # 在黑色方塊上方加入文字
    text = 'oxxo.studio'
    org = (110,160)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255,255,255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(opencv_img, text, org, fontFace, fontScale, color, thickness, lineType)

    img_list.append(opencv_img)

loop = True
while loop:
    for i in img_list:
        cv2.imshow('oxxostudio', i)
        if cv2.waitKey(200) == ord('q'):
            loop = False
            break
# 建立要輸出的影格串列
output = []
for i in img_list:
    img = i
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 因為 OpenCV 為 BGRA，要轉換成 RGBA
    img = Image.fromarray(img)    # 轉換成 PIL 格式
    img = img.convert('RGB')      # 轉換成 RGB ( 如果是 RGBA 會自動將黑色白色變成透明色 )
    output.append(img)            # 加入 output
# 儲存為 gif 動畫圖檔
output[0].save("oxxostudio.gif", save_all=True, append_images=output[1:], duration=200, loop=0, disposal=0)
cv2.destroyAllWindows()
