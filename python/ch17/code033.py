# Copyright © https://steam.oxxostudio.tw

from pytube import YouTube

def onProgress(stream, chunk, remains):
    total = stream.filesize                     # 取得完整尺寸
    percent = (total-remains) / total * 100     # 減去剩餘尺寸 ( 剩餘尺寸會抓取存取的檔案大小 )
    print(f'下載中… {percent:05.2f}', end='\r')  # 顯示進度，\r 表示不換行，在同一行更新

print('download...')
yt = YouTube('https://www.youtube.com/watch?v=R93ce4FZGbc', on_progress_callback=onProgress)
yt.streams.filter().get_highest_resolution().download(filename='oxxostudio.mp4')
# on_progress_callback 參數等於 onProgress 函式
print()
print('ok!')

