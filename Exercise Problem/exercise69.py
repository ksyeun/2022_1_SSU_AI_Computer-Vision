#OpenCV 함수 중에서 cv2.addWeighted() 함수를 사용해서 
# 두 영상을 합성하는 프로그램을 작성하시오
#8번 문제에서 두 개의 트렉바를 추가해서 각 영상의 반영 비율을 조절할 수 있도록 수정 하시오.

import numpy as np, cv2



image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2= cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception ("ERROR: Reading image")

def onChange (pos):
 
    global image, title
    value1 = cv2.getTrackbarPos("Change_image1",title)/100
    value2 = cv2.getTrackbarPos("Change_image2",title)/100
    image = cv2.addWeighted (image1, value1, image2, value2, 0)
    cv2.imshow(title,image)



image = np.zeros (image1.shape, np.uint8)

title = "exercise"
cv2.imshow(title,image)

cv2.createTrackbar("Change_image1", title, 0, 100, onChange)
cv2.createTrackbar("Change_image2", title, 0, 100, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
