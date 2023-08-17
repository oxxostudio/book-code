# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import csv
csvfile = open('csv-demo.csv')     # 開啟 CSV 檔案
raw_data = csv.reader(csvfile)     # 讀取 CSV 檔案
data = list(raw_data)              # 轉換成二維串列
print(data)
'''
[['name', 'id', 'color', 'price'],
 ['apple', '1', 'red', '10'],
 ['orange', '2', 'orange', '15'],
 ['grap', '3', 'purple', '20'],
 ['watermelon', '4', 'green', '30']]
'''

