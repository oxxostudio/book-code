# Copyright © https://steam.oxxostudio.tw

sleep(2)     # 等待兩秒，讓網頁載入完成
# 取得輸入 email 的輸入框
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys('你的 email')    # 輸入 email
print('輸入 email 完成')
# 取得畫面上所有按鈕 ( 使用 elements )
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == '下一步' or i.text == 'Next':
        i.click()   # 如果按鈕是「下一步」或「Next」就點擊
        print('點擊下一步')
        break

