# Copyright © https://steam.oxxostudio.tw

import glob
import os
images = glob.glob('./demo/*')
print(images)

n = 1          # 設定名稱從 1 開始
for i in images:
    os.rename(i, f'./demo/img-{n:03d}.jpg')   # 改名時，使用字串格式化的方式進行三位數補零
    n = n + 1    # 每次重複時將 n 增加 1


