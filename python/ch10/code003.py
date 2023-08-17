# Copyright © https://steam.oxxostudio.tw

c = int(input('輸入 1 ( 公分 ) 或 2 ( 英吋 )：'))    # 使用變數 c 記錄公分還是英吋
length = int(input('輸入長度數值：'))                # 使用變數 length 記錄數值

if c == 1:
    # 套用轉換公式
    print(f'{length} 公分等於 {length*0.394} 英吋 ( {length*0.03281} 英尺、{length*0.01094} 碼 )')
else:
    # 套用轉換公式
    print(f'{length} 英吋等於 {length*2.54} 公分 ( {length/12} 英尺、{length/36} 碼 )')

