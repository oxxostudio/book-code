# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')
a = driver.find_element(By.ID, 'a')
show = driver.find_element(By.ID, 'show')
actions = ActionChains(driver)
actions.click(show).send_keys(['1','2','3','4','5'])    # 輸入 1～5 的鍵盤值 ( 必須是字串 )
actions.pause(1)    # 等待一秒
actions.click(a)    # 點擊按鈕 A
actions.pause(1)    # 等待一秒
actions.send_keys_to_element(show, ['A','B','C','D','E'])   # # 輸入 A～E 的鍵盤值
actions.perform()   # 送出動作

