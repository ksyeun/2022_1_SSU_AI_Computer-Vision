import numpy as np, cv2

image = cv2.imread("images/filter_sharpen.jpg", cv2.IMREAD_COLOR) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

# 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                 # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1               # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1               # 관심영역 너비 범위d
            roi = image[y1:y2, x1:x2].astype("float32")         # 관심영역 형변환

            tmp = cv2.multiply(roi, mask)                       # 회선 적용 - OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0]                    # 출력화소 저장
    return dst                                                  # 자료형 변환하여 반환

# 블러링 마스크 원소 지  
data = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]
mask = np.array(data, np.float32).reshape(3, 3)

b, g, r = cv2.split(image)
blur_b = filter(b, mask)    
blur_g = filter(g, mask)    
blur_r = filter(r, mask)    
blur_b = cv2.convertScaleAbs(blur_b)
blur_g = cv2.convertScaleAbs(blur_g)       
blur_r = cv2.convertScaleAbs(blur_r)     


list_blur = [blur_b, blur_g, blur_r]
blur_image = cv2.merge (list_blur)
blur_imagecv = cv2.filter2D(image, -1, mask)

cv2.imshow("image", image)
cv2.imshow("bluring_user", blur_image)
cv2.imshow("bluring openCV", blur_imagecv)


# sharp
data1 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]

mask = np.array(data1, np.float32)

sharpen_b = filter(b, mask)    
sharpen_g = filter(g, mask)    
sharpen_r = filter(r, mask)    
list_sharpen = [sharpen_b, sharpen_g, sharpen_r]
sharpen_ima = cv2.merge (list_sharpen)
sharpen_imagecv = cv2.filter2D(image, -1, mask)

sharpen= cv2.convertScaleAbs(sharpen_ima)
cv2.imshow("sharpen_User", cv2.convertScaleAbs(sharpen))
cv2.imshow("sharpen openCV", cv2.convertScaleAbs(sharpen_imagecv))
cv2.waitKey(0)