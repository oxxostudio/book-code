# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('logo.jpg', cv2.IMREAD_UNCHANGED)  # 開啟圖片
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)         # 因為是 jpg，要轉換顏色為 BGRA
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # 新增 gray 變數為轉換成灰階的圖片

h = img.shape[0]     # 取得圖片高度
w = img.shape[1]     # 取得圖片寬度

# 依序取出圖片中每個像素
for x in range(w):
    for y in range(h):
        if gray[y, x]>200:
            img[y, x, 3] = 255 - gray[y, x]
            # 如果該像素的灰階度大於 200，調整該像素的透明度
            # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣

cv2.imwrite('oxxostudio.png', img)    # 存檔儲存為 png
cv2.waitKey(0)                        # 按下任意鍵停止
cv2.destroyAllWindows()
