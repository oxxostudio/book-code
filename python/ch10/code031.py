# Copyright © https://steam.oxxostudio.tw

h = float(input('請輸入身高(cm)：'))/100
w = float(input('請輸入體重(kg)：'))
bmi = round(w/(h*h),3)                  # 使用 round 四捨五入到小數點三位
if bmi<18.5:                            # 使用邏輯判斷
    note = '你太輕囉！'
elif bmi>=18.5 and bmi<=25:
    note = '你的體重正常！'
else:
    note = '你有點太重囉～'
print(f'你的 BMI 數值為：{bmi}，{note}')

