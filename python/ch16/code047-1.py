# Copyright © https://steam.oxxostudio.tw

import requests

webUrl = requests.get('https://today.line.me/tw/v2/article/oqay0ro')   # get 文章網址
# 取得文章的原始碼後，使用 split 字串拆分的方式，拆解出 articleId
article_id = webUrl.text.split('<script>')[1].split('id:"article:')[1].split(':')[0]
print(article_id)

# 使用 requests get 留言物件
comment = requests.get(f'https://today.line.me/webapi/comment/list?articleId={article_id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot=0&postType=Article')
json = comment.json()   # 取得內容後，轉換成 json 格式
num = int(json['result']['comments']['count'])   # 取得文章的總數
print(num)   # 印出文章總數