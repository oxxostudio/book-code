# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')
body = driver.find_element(By.TAG_NAME, 'body')
a = driver.find_element(By.ID, 'a')
b = driver.find_element(By.CLASS_NAME, 'btn')
c = driver.find_element(By.CSS_SELECTOR, '.test')
d = driver.find_element(By.NAME, 'dog')
link1 = driver.find_element(By.LINK_TEXT, '我是超連結，點擊會開啟 Google 網站')
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google')

print(a.id)
print(b.text)
print(c.tag_name)
print(d.size)
print(link1.get_attribute('href'))
print(link2.get_attribute('target'))
body.screenshot('./test.png')

