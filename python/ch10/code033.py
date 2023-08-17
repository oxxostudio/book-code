# Copyright © https://steam.oxxostudio.tw

import datetime
import calendar       # import calendar 模組
today = datetime.date.today()
age = input('輸入生日 ( YYYY/MM/DD )：')
age_list = age.split('/')
year = today.year - int(age_list[0])
month = today.month - int(age_list[1])
if month<0:
    year = year - 1
    month = 12 + month
day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
if calendar.isleap(today.year):         # 判斷如果是閏年
    day_list[1] = 29                    # 就將二月份的天數改成 29 天
day = today.day - int(age_list[2])
if day<0:
    month = month - 1
    if month<0:
        year = year - 1
        month = 12 + month
    day = day_list[month] + day

print(f'{year} 歲 {month} 個月 {day} 天')

