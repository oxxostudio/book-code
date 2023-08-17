# Copyright © https://steam.oxxostudio.tw

driver.get('https://twitter.com')
sleep(2)
driver.execute_script(f'window.scrollTo(0, 200)')   # 自動往下捲動 200px
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')   # 取得登入按鈕
login.click()   # 點擊登入按鈕

