# Copyright © https://steam.oxxostudio.tw


# 下方的程式使用「ActionChains」的方式，結果與上述的執行結果相同。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver')
driver.get('https://example.oxxostudio.tw/python/selenium/demo.html')
a = driver.find_element(By.ID, 'a')
add = driver.find_element(By.ID, 'add')
actions = ActionChains(driver)   # 使用 ActionChains 的方式
actions.click(a).pause(1)        # 點擊按鈕 A，出現 a 文字後，暫停一秒
actions.double_click(add).pause(1).click(add).pause(1).click(add)
# 連點 add 按鈕，等待一秒後再次點擊，等待一秒後再次點擊
actions.perform()  # 執行儲存的動作