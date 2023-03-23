# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

cap = cv2.VideoCapture(0)                 # 讀取攝影鏡頭
w = 420
h = 240
draw = np.zeros((h,w,4), dtype='uint8')
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # 設定輸出影片的格式為 MJPG
out = cv2.VideoWriter('output.mov', fourcc, 20.0, (w, h))  # 產生空的影片

if not cap.isOpened():
    print("Cannot open camera")
    exit()

def show_xy(event,x,y,flags,param):
    global dots, draw
    if flags == 1:
        if event == 1:
            dots.append([x,y])
        if event == 4:
            dots = []
        if event == 0 or event == 4:
            dots.append([x,y])
            x1 = dots[len(dots)-2][0]
            y1 = dots[len(dots)-2][1]
            x2 = dots[len(dots)-1][0]
            y2 = dots[len(dots)-1][1]
            cv2.line(draw,(x1,y1),(x2,y2),(0,0,255,255),2)

cv2.imshow('oxxostudio', draw)
cv2.setMouseCallback('oxxostudio', show_xy)

while True:
    ret, img = cap.read()               # 讀取影片的每一個影格
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(img,(w,h))         # 縮小尺寸，加快運算速度
    # 透過 for 迴圈合成影像
    for i in range(w):
        img[:,i,0] = img[:,i,0]*(1-draw[:,i,3]/255) + draw[:,i,0]*(draw[:,i,3]/255)
        img[:,i,1] = img[:,i,1]*(1-draw[:,i,3]/255) + draw[:,i,1]*(draw[:,i,3]/255)
        img[:,i,2] = img[:,i,2]*(1-draw[:,i,3]/255) + draw[:,i,2]*(draw[:,i,3]/255)
    keyboard = cv2.waitKey(5)
    if keyboard == ord('q'):
        break
    if keyboard == ord('r'):
        draw = np.zeros((h,w,4), dtype='uint8')
    cv2.imshow('oxxostudio', img)
    out.write(img)  # 儲存影片

out.release()       # 釋放資源
cap.release()       # 釋放資源
cv2.destroyAllWindows()
