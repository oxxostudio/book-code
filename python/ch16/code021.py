# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')  # 開啟範例網址
a = driver.find_element(By.ID, 'a')                # 取得 id 為 a 的網頁元素 ( 按鈕 A )
b = driver.find_element(By.CLASS_NAME, 'btn')      # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
c = driver.find_element(By.CSS_SELECTOR, '.test')  # 取得 class 為 test 的網頁元素 ( 按鈕 C )
d = driver.find_element(By.NAME, 'dog')            # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
h1 = driver.find_element(By.TAG_NAME, 'h1')        # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, '我是超連結，點擊會開啟 Google 網站')  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google') # 取得超連結文字包含 Google 的網頁元素
select = Select(driver.find_element(By.XPATH, '/html/body/select'))   # 取得 html > body > select 這個網頁元素

a.click()        # 點擊 a
print(a.text)    # 印出 a 元素的內容
time.sleep(0.5)
b.click()        # 點擊 b
print(b.text)    # 印出 b 元素的內容
time.sleep(0.5)
c.click()        # 點擊 c
print(c.text)    # 印出 c 元素的內容
time.sleep(0.5)
d.click()        # 點擊 d
print(d.text)    # 印出 d 元素的內容
time.sleep(0.5)
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(0.5)
h1.click()       # 點擊 h1
time.sleep(0.5)
link1.click()    # 點擊 link1
time.sleep(0.5)
link2.click()    # 點擊 link2
print(link2.get_attribute('href'))   # 印出 link2 元素的 href 屬性

