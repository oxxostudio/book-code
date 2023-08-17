# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome('./chromedriver', options=opt)
driver.get('要爬的網址')

