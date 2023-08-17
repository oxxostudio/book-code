# Copyright © https://steam.oxxostudio.tw

import re

# 輸入字符串
text = '''請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
'''

regex= re.compile(r'[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+')
arr = re.findall(regex, text)
text = ' '.join(arr)

regex= re.compile(r'(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])')
text = re.sub(regex, '', text)

regex= re.compile(r'(\x20)(?=[\(\%\uFF00-\uFFFF])')
text = re.sub(regex, '', text)

text = text.replace(' . ','.')
print(text)

