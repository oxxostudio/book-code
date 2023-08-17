# Copyright © https://steam.oxxostudio.tw

import smtplib
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('你的信箱','你的密碼')
from_addr = '你的信箱'
to_addr = '收件人信箱'
msg = 'Subject:title\nHello\nWorld!'
status = smtp.sendmail(from_addr, to_addr, msg)
if status == {}:
    print('郵件傳送成功！')
else:
    print('郵件傳送失敗...')
smtp.quit()

