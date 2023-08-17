# Copyright © https://steam.oxxostudio.tw

input_str = input('輸入數字 ( 逗號分隔 )：')   # 讓使用者輸入數字，數字間用逗號分隔
nums = input_str.split(',')   # 將輸入的文字，用逗號拆分成串列
for i in range(len(nums)):    # 將串列的每個項目轉換成文字
    nums[i-1] = int(nums[i-1])
nums.sort(reverse=True)       # 將串列從大到小排序
result = nums[0]              # 設定「暫定的最小公倍數」為最大的數字
while True:                   # 執行 while 迴圈
    a = 0                       # 新增 a 變數，當作餘數使用
    for i in nums:              # 依序取出串列中的每個數字
        a = result%i              # 用「暫定的最小公倍數」除以每個數字，求出餘數
        if a != 0:                # 如果餘數不為 0，跳出 for 迴圈再來一次
            break
    if a == 0:                  # 如果全部餘數都為 0，跳出 while 迴圈
        break
    else:
        result = result + nums[0] # 如果餘數不為 0，就將「暫定的最小公倍數」加上最大的數字，然後再來一次
print(result)                 # while 迴圈結束後，印出最小公倍數

