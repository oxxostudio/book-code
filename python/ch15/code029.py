# Copyright © https://steam.oxxostudio.tw

import os
os.chdir('/content/drive/MyDrive/Colab Notebooks')  # 使用 Colab 要換路徑使用，本機環境可以刪除

# 定義轉換為總秒數的函式
def time2sec(t):
    arr = t.split(' --> ')   # 根據「' --> '」拆分文字
    s1 = arr[0].split(',')   # 前方的文字為開始時間
    s2 = arr[1].split(',')   # 後方的文字為結束時間
    # 計算開始時間的總秒數
    start = int(s1[0].split(':')[0])*3600 + int(s1[0].split(':')[1])*60 + int(s1[0].split(':')[2]) + float(s1[1])*0.001
    # 計算結束時間的總秒數
    end = int(s2[0].split(':')[0])*3600 + int(s2[0].split(':')[1])*60 + int(s2[0].split(':')[2]) + float(s2[1])*0.001
    return [start, end]      # 回傳開始時間與結束時間的串列

f = open('oxxostudio.srt','r')  # 使用 open 方法的 r 開啟字幕檔案
srt = f.read()                  # 讀取字幕檔案內容
f.close()                       # 關閉檔案
srt_list = srt.split('\n')      # 將內容根據換行符號 \n 拆分成串列
sec = 1                         # 串列中秒數從第二項開始 ( 串列的第二項的索引值為 1 )
text = 2                        # 串列中文字內容從第三項開始 ( 串列的第三項的索引值為 2 )
sec_list = [[0,0]]              # 定義時間串列的開頭為 [0,0]
text_list = ['']                # 定義字幕內容串列的開頭為空字串 ''
# 使用迴圈，讀取字幕檔案串列的每個項目
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4           # 如果遇到時間內容，就將 sec + 4 ( 因為時間每隔 4 個項目會出現 )
        # 如果兩個串列項目內容前後對不上 ( 前一個結束時間不等於後一個的開始時間 )
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            # 在時間串列中間添加一個開始時間與結束時間內容 ( 表示該區間沒有字幕 )
            sec_list.append([sec_list[-1][1],time2sec(srt_list[i])[0]])
            # 在文字串列中間添加一個空字串 ( 表示該區間沒有字幕 )
            text_list.append('')
        sec_list.append(time2sec(srt_list[i]))  # 添加時間到時間串列
    if i == text:
        text = text + 4               # 如果遇到文字內容，就將 text + 4 ( 因為文字每隔 4 個項目會出現 )
        text_list.append(srt_list[i]) # 添加文字到文字串列

print(sec_list)
print(text_list)

