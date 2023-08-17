# Copyright © https://steam.oxxostudio.tw

import smtplib
from email.mime.text import MIMEText

msg = MIMEText('你好呀！這是用 Python 寄的信～', 'plain', 'utf-8') # 郵件內文
msg['Subject'] = 'test測試'            # 郵件標題
msg['From'] = 'oxxo'                  # 暱稱或是 email
msg['To'] = 'oxxo.studio@gmail.com'   # 收件人 email
msg['Cc'] = 'oxxo.studio@gmail.com, XXX@gmail.com'   # 副本收件人 email ( 開頭的 C 大寫 )
msg['Bcc'] = 'oxxo.studio@gmail.com, XXX@gmail.com'  # 密件副本收件人 email

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('你的信箱','你的密碼')
status = smtp.send_message(msg)    # 改成 send_message
if status == {}:
    print('郵件傳送成功！')
else:
    print('郵件傳送失敗！')
smtp.quit()

