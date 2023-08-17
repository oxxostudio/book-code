# Copyright © https://steam.oxxostudio.tw

text = input('請輸入一串英文或數字：')      # 新增 text 變數，記錄輸入的字串
repeat = []                             # 新增 repeat 變數為空串列
not_repeat = []                         # 新增 not_repeat 變數為空串列
for i in text:                          # 使用 for 迴圈，依序取出每個字元
    a = text.count(i, 0, len(text))     # 判斷字元在字串中出現的次數
    if a>1 and i not in repeat:         # 如果次數大於 1，且沒有存在 repeat 串列中
        repeat.append(i)                  # 將字元加入 repeat 串列
    if a == 1and i not in not_repeat:   # 如果次數等於 1，且沒有存在 not_repeat 串列中
      not_repeat.append(i)              # 將字元加入 not_repeat 串列

print(repeat)
print(not_repeat)

