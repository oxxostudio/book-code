# Copyright © https://steam.oxxostudio.tw

import cv2
bg = cv2.imread('bg.jpg', cv2.IMREAD_UNCHANGED)     # 開啟背景圖
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)           # 轉換成 BGRA

img = cv2.imread('goku.jpg', cv2.IMREAD_UNCHANGED)  # 開啟悟空公仔圖
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 轉換成 BGRA

h = img.shape[0]           # 取得圖片高度
w = img.shape[1]           # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = img[y, x, 2]   # 取得該像素的紅色值
        g = img[y, x, 1]   # 取得該像素的綠色值
        b = img[y, x, 0]   # 取得該像素的藍色值
        if r>20 and r<80 and g<190 and g>110 and b<150 and b>60:
            img[y, x] = bg[y, x]   # 如果在範圍內的顏色，換成背景圖的像素值

cv2.imwrite('oxxostudio.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
