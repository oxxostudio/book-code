# Copyright © https://steam.oxxostudio.tw

sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys('Hello World!I am Robot~ ^_^')      # 在輸入框輸入文字
print('輸入文字')
sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys('/Users/oxxo/Desktop/oxxo.png')   # 提供圖片絕對路徑，上傳圖片
print('上傳圖片')
sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == '推文' or i.text == 'Tweet':
        i.click()    # 點擊推文按鈕
        print('推文完成')
        break
sleep(1)
driver.close()  # 關閉瀏覽器視窗

