from PIL import Image,ImageSequence

gif = []
for i in range(4):
    img = Image.open(f'frame{i}.jpg')  # 開啟圖片
    gif.append(img)                    # 加入串列
# 儲存為 gif
gif[0].save("oxxostudio.gif", save_all=True, append_images=gif[1:], duration=200, loop=0, disposal=0)
