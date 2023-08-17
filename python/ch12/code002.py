# Copyright © https://steam.oxxostudio.tw

import pyautogui

myScreenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
myScreenshot.save('圖片路徑\圖片名稱.png')


