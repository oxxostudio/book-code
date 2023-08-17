# Copyright © https://steam.oxxostudio.tw

a = 10
for i in range(1,a+1):
    print(' '*3*(a-i),end='')
    for j in range(0, i):            # ragne 改成從 0 開始，因為 2 的 0 次方等於 1
        k = 2 ** j                   # 計算 2 的幾次方
        if k==1:
            print(k, end='')
        else:
            print(f'{k:>3d}', end='')
    for j in range(i-2, -1, -1):     # 修改 range，使其最後一位數為 0
        k = 2 ** j                   # 計算 2 的幾次方
        print(f'{k:>3d}', end='')
    print('')

