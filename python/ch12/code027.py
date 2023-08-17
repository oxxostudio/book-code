# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl
wb = openpyxl.load_workbook('test.xlsx', data_only=True)  # 設定 data_only=True 只讀取計算後的數值

s1 = wb['工作表1']
s2 = wb['工作表2']

def get_values(sheet):
    arr = []                      # 第一層串列
    for row in sheet:
        arr2 = []                 # 第二層串列
        for column in row:
            arr2.append(column.value)  # 寫入內容
        arr.append(arr2)
    return arr

print(get_values(s1))       # 印出工作表 1 所有內容
print(get_values(s2))       # 印出工作表 2 所有內容

'''
[[12, 34, 56, 78, 180, 180], [11, 22, 33, 44, 110, 110]]
[['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'], ['a4', 'b4', 'c4'], ['a5', 'b5', 'c5']]
'''

