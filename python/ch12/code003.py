# Copyright © https://steam.oxxostudio.tw

import pyautogui
from time import sleep

for i in range(5):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'./test{i}.png')
    sleep(2)


