import cv2

def bar(value) :
    global title, image
    th1 = cv2.getTrackbarPos('th1', title)
    th2 = cv2.getTrackbarPos('th2', title)
    result = cv2.Canny(image, th1, th2)
    cv2.imshow(title, result)

image = cv2.imread("images/dog_test.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")


title = 'cannay edge'
result = cv2.Canny(image, 100, 150)

cv2.imshow(title, result)

cv2.createTrackbar('th1', title, 50, 255, bar)
cv2.createTrackbar('th2', title, 150, 255, bar)

cv2.waitKey(0)
