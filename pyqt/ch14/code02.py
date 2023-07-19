# Copyright © https://steam.oxxostudio.tw

# 顯示數字函式，n 為點擊按鈕時要帶入的數值
def showNum(n):
    global num
    if n == 'AC':
        num = '0'   # 如果按下數字，數值歸零
    elif n == '=':
        try:
            num = str(eval(num))  # 如果按下等號，使用 eval() 計算結果
        except:
            num = 'error'         # 如果計算結果發生錯誤，回傳 error
    else:
        if num == '0' and n in '0123456789':
            num = n     # 如果數值原本是 0，且按下數字鍵，就讓數字變成所按下的數字
        else:
            num = num + n   # 否則就用字串的方式累加
    label.setText(num)      # QLabel 顯示結果
    if num == 'error':
        num = '0'           # 如果發生錯誤，數值歸零

