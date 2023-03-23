n = 0
for i in source:                  # source 為要轉存的所有圖片陣列 ( opencv 格式，色彩為 RGBA )
    img = Image.fromarray(i)      # 轉換成 PIL 格式
    img.save(f'temp/gif{n}.gif')  # 儲存為 gif
    n = n + 1                     # 改變儲存的檔名編號

output = []                       # 建立空串列
for i in range(n):
    img = Image.open(f'temp/gif{i}.gif')  # 依序開啟每張 gif
    img = img.convert("RGBA")             # 轉換為 RGBA
    output.append(img)                    # 記錄每張圖片內容

# 轉存為 gif 動畫，設定 disposal=2
output[0].save("oxxostudio.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)
