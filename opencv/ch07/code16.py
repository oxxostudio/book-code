# Copyright © https://steam.oxxostudio.tw

import cv2

img1 = cv2.imread('mona.jpg')
img2 = cv2.imread('girl.jpg')
w = img1.shape[1]   # 讀取圖片寬度
h = img1.shape[0]   # 讀取圖片高度

for i in range(w):
    img1[:,i,0] = img1[:,i,0]*((300-i)/300) + img2[:,i,0]*(i/300)  # 藍色按照比例混合
    img1[:,i,1] = img1[:,i,1]*((300-i)/300) + img2[:,i,1]*(i/300)  # 紅色按照比例混合
    img1[:,i,2] = img1[:,i,2]*((300-i)/300) + img2[:,i,2]*(i/300)  # 綠色按照比例混合

cv2.imwrite('oxxostudio.png', save)

show = img1.astype('float32')/255    # 如果要使用 imshow 必須要轉換類型
cv2.imshow('oxxostudio.png', show)

cv2.waitKey(0)       # 按下任意鍵停止
cv2.destroyAllWindows()
