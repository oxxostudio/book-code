# Copyright © https://steam.oxxostudio.tw

import pdfplumber
pdf = pdfplumber.open('oxxostudio.pdf')
page = pdf.pages[1]
table = page.extract_table()
print(table)
pdf.close()

import csv
csvfile = open('test-csv.csv', 'w+')  # 建立 CSV 檔案
write = csv.writer(csvfile)           # 建立寫入物件
for i in table:
    write.writerow(i)                 # 讀取表格每一列寫入 CSV
print('ok')


