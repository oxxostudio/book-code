# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')    # 指向 chromedriver 的位置
driver.get('https://www.google.com')           # 打開瀏覽器，開啟網頁

