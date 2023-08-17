# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl
wb = openpyxl.load_workbook('oxxo.xlsx', data_only=True)

s2 = wb['工作表2']        # 開啟工作表 2
data = [[1,2],[3,4]]     # 二維陣列資料
for y in range(len(data)):
    for x in range(len(data[y])):
        row = 2 + y      # 寫入資料的範圍從 row=2 開始
        col = 2 + x      # 寫入資料的範圍從 column=2 開始
        s2.cell(row, col).value = data[y][x]

wb.save('test2.xlsx')

