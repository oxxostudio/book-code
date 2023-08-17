# Copyright © https://steam.oxxostudio.tw

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome('./chromedriver', options=opt)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('https://twitter.com')
sleep(2)
driver.execute_script(f'window.scrollTo(0, 200)')
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
login.click()
sleep(2)
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys('你的 email')
print('輸入 email 完成')
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == '下一步' or i.text == 'Next':
        i.click()
        print('點擊下一步')
        break
sleep(2)
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys('你的帳號')
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == '下一步' or i.text == 'Next':
            i.click()
            print('驗證使用者帳號，點擊下一步')
            break
    sleep(2)
except:
    print('ok')
    sleep(2)
pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys('你的密碼')
print('輸入密碼')
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == '登入' or i.text == 'Log in':
        i.click()
        print('點擊登入')
        break
sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys('Hello World!I am Robot~ ^_^')
print('輸入文字')
sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys('/Users/oxxo/Desktop/oxxo.png')
print('上傳圖片')
sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == '推文' or i.text == 'Tweet':
        i.click()
        print('推文完成')
        break
sleep(1)
driver.close()

