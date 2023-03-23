# Copyright © https://steam.oxxostudio.tw

import cv2

cv2.namedWindow('oxxostudio')  # 建立一個名為 oxxostudio 的視窗

while True:
    keycode = cv2.waitKey(0)   # 持續等待，直到按下鍵盤按鍵才會繼續
    c = chr(keycode)           # 將 ASCII 代碼轉換成真實字元
    print(c, keycode)          # 印出結果
    if keycode == 27:
        break                  # 如果代碼等於 27，結束迴圈 ( 27 表示按鍵 ESC )

cv2.destroyAllWindows()
