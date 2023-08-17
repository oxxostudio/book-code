# Copyright © https://steam.oxxostudio.tw

while output!=0:      # 使用 while 迴圈，如果 output 等於 0 才會停止
  a = input('請輸入數字 ( 格式 a,b,c... )：')
  b = a.split(',')
  output = 0
  for i in b:
      output += int(i)
  print(f'數字總和為：{output}')

