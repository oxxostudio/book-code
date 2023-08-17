# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl

wb = openpyxl.load_workbook('test.xlsx', data_only=True)

s1 = wb['工作表1']
v = s1.iter_rows(min_row=1, min_col=1, max_col=2, max_row=2)  # 取出四格內容
print(v)
for i in v:
    for j in i:
        print(j.value)
'''
12
34
11
22
'''

