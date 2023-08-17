# Copyright © https://steam.oxxostudio.tw

input_str = input('輸入數字 ( 逗號分隔 )：')     # 讓使用者輸入數字，數字間用逗號分隔
nums_arr = input_str.split(',')               # 將輸入的文字，用逗號拆分成串列
for i in range(len(nums_arr)):                # 將串列的每個項目轉換成文字
    nums_arr[i-1] = int(nums_arr[i-1])
nums_arr.sort()                # 將串列從小到大排序
result = nums_arr[0]           # 建立變數 result，內容為輸入的第一個數字 ( 數字的最小值 )
arr = [result, 1]              # 建立一個變數 arr 為串列，內容預設為 [ 輸入的最小值, 1 ]
for i in range(2,result+1):    # 使用 for 迴圈，找出 result 數字的每個因數
    if result%i == 0:          # 找因數的方法，將 result 依序除以 2、3、4...result
        result = int(result/i) # 如果餘數為 0 ( 整除 )，表示這個數字為因數
        arr.append(i)          # 將因數加入 arr 串列中，並更新 result 為除以因數的數值
        arr.append(result)     # 也將 result 加入 arr 串列 ( 因為商也算是因數 )
arr.sort(reverse=True)         # 完成後將 arr 從大到小排序

for j in arr:                # 依序取出 arr 串列中的每個數字
    a = 0                    # 建立 a 變數，記錄餘數
    output = 1               # 建立 output 變數，記錄最大公因數 ( 預設 1 )
    for i in nums_arr:       # 依序將輸入的數字除以 arr 串列中的數字
        a = a + i%j          # 將餘數加入 a 變數 ( 如果沒有餘數，a 就一直會是 0 )
        output = j           # 將 output 等於目前的因數
    if a == 0:               # 如果 a 為 0 表示都整除，將 result 等於 output
        result = output
        break
print(result)                # 印出最大公因數

