# Copyright © https://steam.oxxostudio.tw

import cv2

mona = cv2.imread('mona.jpg')
logo = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)  # 使用 cv2.IMREAD_UNCHANGED 讀取 png，保留 alpha 色版
mona_w = mona.shape[1]  # 蒙娜麗莎寬度
mona_h = mona.shape[0]  # 蒙娜麗莎高度
logo_w = logo.shape[1]  # logo 寬度
logo_h = logo.shape[0]  # logo 高度
dh = int((mona_h - logo_h) / 2)  # 如果 logo 要垂直置中，和上方的距離
h = dh + logo_h         # 計算蒙娜麗莎裡，logo 所在的高度位置

# 透過迴圈，根據背景透明度，計算出該像素的顏色
for i in range(logo_w):
    mona[dh:h,i,0] = mona[dh:h,i,0]*(1-logo[:,i,3]/255) + logo[:,i,0]*(logo[:,i,3]/255)
    mona[dh:h,i,1] = mona[dh:h,i,1]*(1-logo[:,i,3]/255) + logo[:,i,1]*(logo[:,i,3]/255)
    mona[dh:h,i,2] = mona[dh:h,i,2]*(1-logo[:,i,3]/255) + logo[:,i,2]*(logo[:,i,3]/255)

cv2.imwrite('oxxostudio.png', mona)

mona = mona.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('oxxostudio', mona)

cv2.waitKey(0)
cv2.destroyAllWindows()
