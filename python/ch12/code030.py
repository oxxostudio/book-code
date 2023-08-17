# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl

wb = openpyxl.Workbook()    # 建立空白的 Excel 活頁簿物件
wb.save('empty.xlsx')       # 儲存檔案

