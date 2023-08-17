# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl

wb = openpyxl.load_workbook('oxxo.xlsx')    # 開啟現有的 Excel 活頁簿物件
wb.save('new.xlsx')                        # 儲存檔案

