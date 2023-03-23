# Copyright © https://steam.oxxostudio.tw

import cv2
img = cv2.imread('meme.jpg')
output_ROTATE_90_CLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
output_ROTATE_90_COUNTERCLOCKWISE = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
output_ROTATE_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('output_1.jpg', output_ROTATE_90_CLOCKWISE)
cv2.imwrite('output_2.jpg', output_ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('output_3.jpg', output_ROTATE_180)
