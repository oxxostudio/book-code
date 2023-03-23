from PIL import Image,ImageSequence

gif = Image.open('dot.gif')                # 讀取動畫圖檔

i = 0                                      # 設定編號變數
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGB')           # 取出每一格轉換成 RGB
    frame.save(f'frame{i}.jpg', quality=65, subsampling=0)  # 儲存為 jpg
    i = i + 1                              # 編號增加 1
