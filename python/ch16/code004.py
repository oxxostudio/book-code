# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get('爬取的網址')
# 從載入後的動態網頁裡，找到指定的元素
imgCount = driver.find_element(By.CSS_SELECTOR, 'CSS 選擇器')

