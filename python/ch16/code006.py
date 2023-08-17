# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from time import sleep
submitBtn = driver.find_element(By.CSS_SELECTOR, '#submitBtn')
sleep(1)     # 等待一秒
submitBtn.click()
sleep(0.5)   # 等待 0.5 秒
submitBtn.click()

