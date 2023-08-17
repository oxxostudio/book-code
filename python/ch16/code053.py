# Copyright © https://steam.oxxostudio.tw

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys('你的密碼')
print('輸入密碼')
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == '登入' or i.text == 'Log in':
        i.click()
        print('點擊登入')
        break

