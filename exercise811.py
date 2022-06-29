import numpy as np,  cv2

image = cv2.imread('images/rotate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일을 읽기 에러")


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

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)                     # 목적 영상 생성
    radian = (degree/180) * np.pi                               # 회전 각도 - 라디언

    rows, cols = img.shape[:2]
    cen = (100, 100)
    angle = 30
    scale = 1
    rot_mat = cv2.getRotationMatrix2D(cen, angle, scale) 
    inv_mat = cv2.invertAffineTransform(rot_mat)

    dst = np.zeros (img.shape, img.dtype)

    for i in range(rows):                              # 목적 영상 순회 - 역방향 사상
        for j in range(cols):
            pt = np.dot(inv_mat, (j, i, 1))
            if contain(pt, img.shape):                      # 입력 영상의 범위 확인
                dst[i, j] = bilinear_value(img, pt)           # 화소값 양선형 보간

    return dst



rot = [100, 100]

size = image.shape[::-1]
dst1 = rotate_pt(image, 30, rot )                   


cv2.imshow("image", image)
cv2.imshow("dst1-rotated on rot", dst1)
cv2.waitKey(0)