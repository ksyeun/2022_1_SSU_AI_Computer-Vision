#exercise 5-7
import numpy as np
import cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception ("영상파일 처리 오류")
blue, green, red = cv2.split(logo)

dummy= np.zeros((red.shape), np.uint8)

list_red= [dummy, dummy, red]
list_green= [dummy, green, dummy]
list_blue= [blue, dummy, dummy]

blue_img = cv2.merge(list_blue)
green_img = cv2.merge(list_green)
red_img = cv2.merge(list_red)

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img",green_img)
cv2.imshow("red_img", red_img)

cv2.waitKey()