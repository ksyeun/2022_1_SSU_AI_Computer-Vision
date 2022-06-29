#첨부된 2개 얼굴 이미지(faceImage1.jpg, faceImage2.jpg)에서 
# skin color 영역을 검출하라. 


import numpy as np, cv2

image1 = cv2.imread ("images/faceimage1.jpg", cv2.IMREAD_COLOR)
image2 = cv2.imread ("images/faceImage2.jpg", cv2.IMREAD_COLOR)
if image1 is None or image2 is None: raise Exception ("Error")

def skin_detect (image):
    HST_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v =cv2.split(HST_image)
    skincolor = np.zeros (h.shape, np.uint8)
    (x, y) = h.shape
    for i in range (0, x):
        for j in range (0, y):
            if (h[i][j]>6) and (h[i][j]<40) and (s[i][j]>10) and (s[i][j]<150) and (v[i][j]>80) and (v[i][j]<255):
                skincolor [i][j] = 255
            else:
                skincolor[i][j] = 0
    result = cv2.bitwise_and(image, image, mask=skincolor)
    return result


pic = skin_detect(image1)
pic2 = skin_detect(image2)

cv2.imshow("first", pic)
cv2.imshow("second", pic2)
cv2.waitKey()