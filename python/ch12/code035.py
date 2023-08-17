# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl
wb = openpyxl.load_workbook('oxxo.xlsx', data_only=True)

s3 = wb.create_sheet('工作表3')     # 新增工作表 3
data = [[1,2,3],[4,5,6],[7,8,9]]   # 二維陣列資料
for i in data:
    s3.append(i)                   # 逐筆添加到最後一列

wb.save('test2.xlsx')

