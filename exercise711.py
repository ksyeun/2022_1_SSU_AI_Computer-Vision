import numpy as np, cv2, time

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

# 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                 # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1               # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1               # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32")         # 관심영역 형변환

            tmp = cv2.multiply(roi, mask)                       # 회선 적용 - OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0]                    # 출력화소 저장
    return dst                                                  # 자료형 변환하여 반환


def differential1(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    dst = cv2.magnitude(dst1, dst2)                # 회선 결과인 두 행렬의 크기 계산
    dst1, dst2 = np.abs(dst1), np.abs(dst2)  # 회선 결과 행렬 양수 변경

    dst = np.clip(dst, 0, 255).astype("uint8")
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")
    return dst, dst1, dst2

def differential2(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)                     # 사용자 정의 회선 함수
    dst2 = filter(image, mask2)
    dst = cv2.magnitude(dst1, dst2)                 # 회선 결과 두 행렬의 크기 계산

    dst = cv2.convertScaleAbs(dst)                      # 윈도우 표시 위해 OpenCV 함수로 형변환 및 saturation 수행
    dst1 = cv2.convertScaleAbs(dst1)
    dst2 = cv2.convertScaleAbs(dst2)
    return dst, dst1, dst2


    
ro_data1 = [-1, 0, 0,
          0, 1, 0,
          0, 0, 0]
ro_data2 = [ 0, 0, -1,
          0, 1, 0,
          0, 0, 0]


pre_data1 = [-1, 0, 1,                         # 프리윗 수직 마스크
         -1, 0, 1,
         -1, 0, 1]
pre_data2 = [-1,-1,-1,                        # 프리윗 수평 마스크
          0, 0, 0,
          1, 1, 1]


so_data1 = [-1, 0, 1,                  # 수직 마스크
         -2, 0, 2,
         -1, 0, 1]
so_data2 = [-1,-2,-1,                 # 수평 마스크
          0, 0, 0,
          1, 2, 1]
          
dst_01, dst1, dst2 = differential1(image, ro_data1, ro_data2)  		# 회선 수행 및 두 방향의 크기 계산
dst_02, dst1, dst2 = differential2(image, pre_data1, pre_data2)
dst_03, dst1, dst2 = differential2(image, so_data1, so_data2)    

cv2.imshow("image", image)
cv2.imshow("roberts edge", dst_01)
cv2.imshow("prewitt edge", dst_02)
cv2.imshow("soble edge", dst_03)
cv2.waitKey(0)