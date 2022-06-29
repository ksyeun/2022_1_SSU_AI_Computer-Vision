
import numpy as np,  cv2

def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x -1
    if y >= img.shape[0]-1: y = y - 1

    P1, P3, P2, P4 = np.float32(img[y:y+2,x:x+2].flatten())
   ## 4개의 화소 가져옴 – 화소 직접 접근
   #  P1 = float(img[y, x] )                         # 상단 왼쪽 화소
   #  P3 = float(img[y + 0, x + 1])                  # 상단 오른쪽 화소
   #  P2 = float(img[y + 1, x + 0])                  # 하단 왼쪽 화소
   #  P4 = float(img[y + 1, x + 1])                  # 하단 오른쪽 화소

    alpha, beta = pt[1] - y,  pt[0] - x                   # 거리 비율
    M1 = P1 + alpha * (P3 - P1)                      # 1차 보간
    M2 = P2 + alpha * (P4 - P2)
    P  = M1 + beta  * (M2 - M1)                     # 2차 보간
    return  np.clip(P, 0, 255)                       # 화소값 saturation후 반환

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)                     # 목적 영상 생성
    radian = (degree/180) * np.pi                               # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)   # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):                              # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)                # 중심좌표 평행이동,
            y = -jj * sin + ii * cos               # 회선 변환 수식
            x =  jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):                      # 입력 영상의 범위 확인
                dst[i, j] = bilinear_value(img, [x, y])           # 화소값 양선형 보간
    return dst

image = cv2.imread('images/rotate.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일을 읽기 에러")

BGR = cv2.split(image)    

center = np.divmod(BGR[0].shape[:-1], 2)[0]
rotate_B = rotate_pt(BGR[0], 20, center)                             # 영상 중심 기준 회전 변환          
rotate_G = rotate_pt(BGR[1], 20, center)                  
rotate_R = rotate_pt(BGR[2], 20, center)              

list_bgr = [rotate_B, rotate_G, rotate_R]

dst = cv2.merge(list_bgr)

cv2.imshow("image", image)
cv2.imshow("dst-rotated on center", dst)
cv2.waitKey(0)