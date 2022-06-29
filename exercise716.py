import numpy as np, cv2

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")


th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]  # 영상 이진화


data = [0, 1, 0,                                               # 마스크 선언 및 초기화
        1, 1, 1,
        0, 1, 0]
mask = np.array(data, np.uint8).reshape(3, 3)


mask2 = np.array([[0, 1, 0],                         # 마스크 초기화
                 [1, 1, 1],
                 [0, 1, 0]]).astype("uint8")

def morphology(img, mask, input):
    dst = np.zeros(img.shape, np.uint8)
    if (input==0): #erode
            mask=None
            if mask is None: mask = np.ones((3, 3), np.uint8)
            mcnt = cv2.countNonZero(mask)
            num1 = 255
            num2 = 0
            
    else:
        if mask is None: mask = np.ones((3, 3), np.uint8)
        mcnt = 0 
        num1= 0
        num2 = 255
        
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    for i in range(ycenter, img.shape[0] - ycenter):    # 입력 행렬 반복 순회
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1       # 마스크 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1       # 마스크 너비 범위
            roi = img[y1:y2, x1:x2]                     # 마스크 영역
            temp = cv2.bitwise_and(roi, mask)
            cnt  = cv2.countNonZero(temp)
            dst[i, j] = num1 if (cnt == mcnt) else num2  # 출력 화소에 저장
    return dst
    
   
dst3 = morphology(th_img, mask, 0)                                  
dst4 = morphology(th_img, mask2, 1)        

cv2.imshow("erode", dst3)
cv2.imshow("dilate", dst4)

cv2.waitKey(0)


