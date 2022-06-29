import numpy as np, cv2

def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)            # 목적 영상 생성
    for i in range(img.shape[0]):                          
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i) , pt)
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]
    return dst

image = cv2.imread('images/translate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")

dst1 = translate(image, (50, 60))    

dx, dy = 50, 60 
rows,cols = image.shape[0:2] 
mtrx = np.float32([[1, 0, dx],
                   [0, 1, dy]])  
dst2 = cv2.warpAffine(image, mtrx, (cols+dx, rows+dy),cv2.INTER_LINEAR)   

cv2.imshow("dst1: trans to (50, 60)", dst1)
cv2.imshow("dst2: trans to (50, 60)", dst2)


cv2.waitKey(0)

