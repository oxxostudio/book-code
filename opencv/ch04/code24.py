# Copyright © https://steam.oxxostudio.tw

import cv2
import numpy as np

img = cv2.imread('japan.jpeg')

def floodFill(source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE):
    result = source.copy()
    cv2.floodFill(result, mask=mask, seedPoint=seedPoint, newVal=newVal, loDiff=loDiff, upDiff=upDiff, flags=flags)
    return result

h, w = img.shape[:2]                     # 取得原始影像的長寬
mask = np.zeros((h+2,w+2,1), np.uint8)   # 製作 mask，長寬都要加上 2
output = floodFill(img, mask, (100,10), (0,0,255), (100,100,60), (100,100,100))

cv2.imshow('oxxostudio', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
