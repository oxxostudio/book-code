# Copyright © https://steam.oxxostudio.tw

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

html = '''
<h1>hello</h1>
<div>這是 HTML 的內容</div>
<div style="color:red">紅色的字</div>
'''
msg = MIMEMultipart()                         # 使用多種格式所組成的內容
msg.attach(MIMEText(html, 'html', 'utf-8'))   # 加入 HTML 內容
# 使用 python 內建的 open 方法開啟指定目錄下的檔案
with open('/content/drive/MyDrive/Colab Notebooks/meme.jpg', 'rb') as file:
    img = file.read()
attach_file = MIMEApplication(img, Name='meme.jpg')    # 設定附加檔案圖片
msg.attach(attach_file)                       # 加入附加檔案圖片

msg['Subject']='附件是一張搞笑的圖'
msg['From']='oxxo'
msg['To']='oxxo.studio@gmail.com'

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('oxxo.studio@gmail.com','你申請的應用程式密碼')
status = smtp.send_message(msg)
print(status)
smtp.quit()

