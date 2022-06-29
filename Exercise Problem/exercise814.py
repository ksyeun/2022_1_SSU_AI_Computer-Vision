import numpy as np, cv2
def calc_length(pts):
    d1 = np.subtract(pts[0], pts[1]).astype(float)        # 두 좌표간 차분 계산
    #d2 = np.subtract(pts[2], pts[0]).astype(float)
    #angle1 = cv2.fastAtan2(d1[1], d1[0])  # 차분으로 각도 계산
    #angle2 = cv2.fastAtan2(d2[1], d2[0])
    #return (angle2 - angle1)  # 두 각도 간의 차분
    length =(d1[0]**2+d1[1]**2)**0.5
    return (length)

def calc_gragient(pts):
    d1 = np.subtract(pts[0], pts[1]).astype(float)        # 두 좌표간 차분 계산
    angle = cv2.fastAtan2(d1[1], d1[0])  # 차분으로 각도 계산
    return (angle)


def translate (img, pt):
    d1 = np.subtract(pts[0], pts[1]).astype(int)     
    dx = d1[0]
    dy = d1[1]
    rows,cols = img.shape[0:2] 
    mtrx = np.float32([[1, 0, dx],
                    [0, 1, dy]])  
    dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy),cv2.INTER_LINEAR)   
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
        dst = translate (image, pts)
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