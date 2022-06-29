#영상 파일을 읽어 들여서 HSV 컬로 공간으로 변환하고, 
#Hue와 Saturation 채널로 2차원 히스토그램을 구하시오.
#즉, 2차원 히스토그램의 Hue(세로)와 Saturaion(가로)을 
# 2개 축으로 구성하고, 빈도값을 밝기로 표현해서 오른쪽 그림과 같이 2차원 그래프로 그리시오.

import numpy as np, cv2

hsclae = 10

BGR_img = cv2.imread("images/test.jpg", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception ("Error reading file")

HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([HSV_img], [0, 1], None, [180, 256], [0, 180, 0, 256])

hue, saturation, intensity = cv2.split(HSV_img)

hsv_map = np.zeros((180,256,3), np.uint8)
h, s = np.indices(hsv_map.shape[:2])
hsv_map[:,:,0] = h
hsv_map[:,:,1] = s
hsv_map[:,:,2] = 255
hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)

new = np.clip (hist, 0, 1)
new = hsv_map * new[:,:, np.newaxis]
new = np.uint8(new)
cv2.imshow('hist', new)
cv2.waitKey(0)
