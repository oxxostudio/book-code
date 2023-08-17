# Copyright © https://steam.oxxostudio.tw

local_table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
        'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
        'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
id_number = input('輸入身分證字號：')
check = False                         # 新增 check=False 變數，與 while 迴圈搭配
while True:                           # 使用 while 迴圈
    id_arr = list(id_number)            # 新增 id_arr 變數，將身分證字號轉換成串列存入
    if len(id_arr)!=10: break           # 判斷如果 id_arr 長度不等於 10，就跳出 while 迴圈
    local = str(local_table[id_arr[0]])    # 將對應的二位數字轉換成字串
    check_arr = list(local)                # 將字串轉換成陣列，例如 '10' 會轉換成 ['1','0']
    check_arr[0] = int(check_arr[0])       # 將串列中的第一個項目轉換成數字
    check_arr[1] = int(check_arr[1]) * 9   # 將串列中的第二個項目轉換成數字
    sex = id_arr[1]                   # 取得第二碼數字
    if sex!='1' and sex!='2': break   # 判斷如果不是 '1' 也不是 '2' 就跳出 while 迴圈
    check_arr.append(int(sex)*8)                 # 將 sex 內容轉換成數字並乘以 8，存入 check_arr 裡
    for i in range(7):                           # 使用 for 迴圈，重複七次
        check_arr.append(int(id_arr[i+2])*(7-i))   # 每次重複，按照檢查碼程式，將數字乘以對應的數值
    check_num = 10 - sum(check_arr)%10           # 計算使用者輸入的檢查碼
    if check_num != int(id_arr[9]): break        # 如果檢查碼不相同，跳出 while 迴圈
    check = True                                 # 如果迴圈都沒有跳出，讓 check 等於 True。
    break                                        # 結束後跳出迴圈

if check == False:                             # while 迴圈結束後，如果 check 等於 Fasle，表示身分證字號錯誤
    print('身分證字號格式錯誤')
else:
    print('身分證字號正確')

