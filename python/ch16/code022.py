# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')
a = driver.find_element(By.ID, 'a')
add = driver.find_element(By.ID, 'add')
a.click()     # 點擊按鈕 A，出現 a 文字
sleep(1)
add.click()   # 點擊 add 按鈕，出現 數字 1
add.click()   # 點擊 add 按鈕，出現 數字 2
sleep(1)
add.click()   # 點擊 add 按鈕，出現 數字 3
sleep(1)
add.click()   # 點擊 add 按鈕，出現 數字 4


