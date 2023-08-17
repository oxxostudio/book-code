# Copyright © https://steam.oxxostudio.tw

import requests

webUrl = requests.get('https://today.line.me/tw/v2/article/oqay0ro')   # get 文章網址
# 取得文章的原始碼後，使用 split 字串拆分的方式，拆解出 articleId
article_id = webUrl.text.split('<script>')[1].split('id:"article:')[1].split(':')[0]
print(article_id)


