# Copyright © https://steam.oxxostudio.tw

import requests

webUrl = requests.get('https://today.line.me/tw/v2/article/oqay0ro')
article_id = webUrl.text.split('<script>')[1].split('id:"article:')[1].split(':')[0]
print(article_id)

commentUrl = requests.get(f'https://today.line.me/webapi/comment/list?articleId={article_id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot=0&postType=Article')
json = commentUrl.json()
num = int(json['result']['comments']['count'])
print(num)

# 定義函式，給予一個參數
def getComment(n):
    # 使用字串格式化的方式，讓網址會根據不同的參數而有所不同
    commentUrl = requests.get(f'https://today.line.me/webapi/comment/list?articleId={article_id}&sort=POPULAR&direction=DESC&country=TW&limit=30&pivot={n}&postType=Article')
    json = commentUrl.json()     # 取得對應網址的 json 內容
    comments = json['result']['comments']['comments']   # 取得該網址下所有留言
    for i in comments :
        # 印出留言者名稱以及留言內容
        print('<' + i['displayName'] + '>\n' + i['contents'][0]['extData']['content'])
        print('----------------')

for i in range(0, num, 30):
    getComment(i)    # 從 0 開始，每隔 30 筆取一次
