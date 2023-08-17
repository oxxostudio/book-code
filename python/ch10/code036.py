# Copyright © https://steam.oxxostudio.tw

local_table = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,
        'J':18,'K':19,'L':20,'M':21,'N':22,'O':35,'P':23,'Q':24,'R':25,
        'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33}
while True:       # 新增 while 迴圈，就可以重複輸入
    id_number = input('輸入身分證字號：')
    check = False
    while True:
        try:          # 使用 try
            id_arr = list(id_number)
            if len(id_arr)!=10: break
            local = str(local_table[id_arr[0]])
            check_arr = list(local)
            check_arr[0] = int(check_arr[0])
            check_arr[1] = int(check_arr[1]) * 9
            sex = id_arr[1]
            if sex!='1' and sex!='2': break
            check_arr.append(int(sex)*8)
            for i in range(7):
                check_arr.append(int(id_arr[i+2])*(7-i))
            check_num = 10 - sum(check_arr)%10
            if check_num != int(id_arr[9]): break
            check = True
            break
        except:      # 使用 except，如果發生例外狀況，跳出迴圈
            break

    if check == False:
        print('身分證字號格式錯誤')
    else:
        print('身分證字號正確')

