# Copyright © https://steam.oxxostudio.tw

while True:
    try:
        num = float(input('請輸入用電度數：'))
        output = 0
        if num<=200:
            output = num*3.2
        elif num>200 and num<=300:
            output = 200*3.2 + (num-200)*3.4
        else:
            output = 200*3.2 + 100*3.4 + (num-300)*3.6
        print(f'用電 {num} 度共 {output} 元')
    except:
        break

