# Copyright © https://steam.oxxostudio.tw

sleep(2)     # 等待兩秒頁面載入後繼續
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys('你的帳號')    # 輸入帳號
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == '下一步' or i.text == 'Next':
            i.click()  # 如果按鈕是「下一步」或「Next」就點擊
            print('驗證使用者帳號，點擊下一步')
            break
    sleep(2)       # 等待兩秒頁面載入後繼續
except:
    print('ok')
    sleep(2)       # 如果沒有出現安全性畫面，等待兩秒頁面載入後繼續

