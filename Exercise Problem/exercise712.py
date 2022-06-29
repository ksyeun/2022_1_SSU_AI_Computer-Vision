import numpy as np, cv2

image = cv2.imread("images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")


dst3 = cv2.Laplacian(image, cv2.CV_16S, 1)      # OpenCV 라플라시안 수행 함수
canny2 = cv2.Canny(image, 100, 150)                 # OpenCV 캐니 에지

cv2.imshow("image", image)
cv2.imshow("Laplacian_OpenCV", cv2.convertScaleAbs(dst3))
cv2.imshow("OpenCV_Canny", canny2)           # OpenCV 캐니 에지
cv2.waitKey(0)
