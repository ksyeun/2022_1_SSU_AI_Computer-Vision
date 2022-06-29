
import numpy as np, cv2
def contain(p, shape):                              # 좌표(y,x)가 범위내 인지 검사
    return 0<= p[0] < shape[0] and 0<= p[1] < shape[1]

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x -1
    if y >= img.shape[0]-1: y = y - 1

    P1, P3, P2, P4 = np.float32(img[y:y+2,x:x+2].flatten())
    alpha, beta = pt[1] - y,  pt[0] - x                   # 거리 비율
    M1 = P1 + alpha * (P3 - P1)                      # 1차 보간
    M2 = P2 + alpha * (P4 - P2)
    P  = M1 + beta  * (M2 - M1)                     # 2차 보간
    return  np.clip(P, 0, 255)                       # 화소값 saturation후 반환


def calc_length(pts):
    d1 = np.subtract(pts[0], pts[1]).astype(float)        # 두 좌표간 차분 계산
    length =(d1[0]**2+d1[1]**2)**0.5
    return (length)

def calc_gragient(pts):
    d1 = np.subtract(pts[0], pts[1]).astype(float)        # 두 좌표간 차분 계산
    angle = cv2.fastAtan2(d1[0], d1[1])  # 차분으로 각도 계산
    return (angle)


def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)                     # 목적 영상 생성
    radian = (degree/180) * np.pi                               # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)   # 사인, 코사인 값 미리 계산
    for i in range(img.shape[0]):                                       # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x =  j * cos + i * sin                  # 회선 변환 수식
            if contain((y, x), img.shape):             # 입력 영상의 범위 확인
                dst[i, j] = bilinear_value(img, [x, y])           # 화소값 양선형 보간
    return dst



def draw_point(x, y):
    pts.append([x,y])
    print("좌표:", len(pts), [x,y])
    cv2.circle(tmp, (x, y), 2, 255, 2)  # 중심 좌표 표시

def onMouse(event, x, y, flags, param):
    global tmp, pts
    if (event == cv2.EVENT_LBUTTONDOWN  and len(pts) == 0):  
        draw_point(x, y)
    if (event == cv2.EVENT_LBUTTONUP and len(pts) == 1): 
        draw_point(x, y)
    if len(pts) == 2:
        cv2.line(image, tuple(pts[0]), tuple(pts[1]), 255)
        legth = calc_length(pts)  # 회전각 계산
        print("length : %3.2f" % legth)
        angle = calc_gragient(pts)  # 회전각 계산
        print("gradient : %3.2f" % angle)
        dst = rotate(image, angle)  # 사용자 정의 함수 회전 수행
        cv2.imshow("image", dst) 
        tmp = np.copy(image)  # 임시 행렬 초기화
        pts = []

image = cv2.imread('images/rotate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")
tmp = np.copy(image)
pts = []

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)