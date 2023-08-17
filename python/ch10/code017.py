# Copyright © https://steam.oxxostudio.tw

a = 15                       # 新增變數 a，設定金字塔有幾層
b = a*2+1                    # 新增變數 b，計算底部有幾個星星
for i in range(1,b,2):       # 使用 for 迴圈，從 1～b，每隔 2 個一數
    move = round((b-i)/2)-1  # 計算星星的位移空白 ( 要將星星都置中 )
    print(f' '*move, end='') # 印出星星前方的位移空白 ( 不換行 )
    print('*'*i)             # 加上「幾個星星」( 乘以 i )

