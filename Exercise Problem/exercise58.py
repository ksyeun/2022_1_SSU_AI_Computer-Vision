#다음 영상에서 특정 영역의 타원만을 복사하여,
#새 창에 표시하는 프로그램을 완성하시오.
#cv2.bitwise_and(), or()등을 사

import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception ("영상 파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)
center = (190, 170)
size = (50, 100)


mark = (1, 1, 1)
back = np.zeros(image.shape[:2], np.uint8)
cv2.ellipse(back, center, size, 0, 0, 360, mark, -1)

split_image = cv2.split(image)

print(image)
print(split_image[0])

blue = cv2.bitwise_or(split_image[0], back, mask=back)
green = cv2.bitwise_or(split_image[1], back,  mask=back)
red = cv2.bitwise_or(split_image[2], back,  mask=back)

list_bgr = [blue, green, red]
dst = cv2.merge(list_bgr)

cv2.imshow("image",image)
cv2.imshow("dst",dst)
cv2.waitKey()