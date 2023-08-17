# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可刪除

import openpyxl
wb = openpyxl.load_workbook('oxxo.xlsx', data_only=True)

s2 = wb['工作表2']
s2['d1'] = '=sum(a1:c1)'    # 寫入公式
s2['d2'] = '=sum(a2:c2)'    # 寫入公式
s2['d3'] = '=sum(a3:c3)'    # 寫入公式
s2['d4'] = '=sum(a4:c4)'    # 寫入公式
s2['d5'] = '=sum(a5:c5)'    # 寫入公式

wb.save('test2.xlsx')

