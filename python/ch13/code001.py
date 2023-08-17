# Copyright © https://steam.oxxostudio.tw

import glob
# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除
jpg = glob.glob('./demo/*.[jJ][pP][gG]')  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(images)
'''
['./demo/pic-001.jpg', './demo/pic-002.jpg', './demo/pic-003.jpg',
'./demo/pic-004.jpg', './demo/pic-005.jpg', './demo/pic-006.jpg',
'./demo/pic-007.jpg', './demo/pic-008.jpg', './demo/pic-009.jpg',
'./demo/pic-010.jpg']
'''

