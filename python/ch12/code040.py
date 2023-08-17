# Copyright © https://steam.oxxostudio.tw

import csv
import openpyxl

csvfile = open('csv-demo.csv')     # 開啟 CSV 檔案
raw_data = csv.reader(csvfile)     # 讀取 CSV 檔案
data = list(raw_data)              # 轉換成二維串列

wb = openpyxl.Workbook()           # 建立空白的 Excel 活頁簿物件
sheet = wb.create_sheet('csv')     # 建立空白的工作表
for i in data:
    sheet.append(i)                # 逐筆添加到最後一列

wb.save('test2.xlsx')


