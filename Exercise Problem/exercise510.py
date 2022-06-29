#pc카메라로 영상을 읽어서 특정 부분(관심 영역)의 합과 평균을 구하는 프로그램을 작성하시오
#1. 관심 영역은 200,100 좌표에서 200x100 크기로 한다.
#2. cv2.mean()함수를 사용하여 평균을 구하시오.
#3. cv2.mean()함수를 상용하지 않고 영상의 원소 순회 방법으로 평균을 구하시오

import numpy as np, cv2
capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception ("No camera")
while True:

    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break
    mask = np.zeros(frame.shape[:2], np.uint8)
    mask[200:400, 100:200] = 1
    sum = cv2.sumElems(frame[200:399, 100:199])
    print("관심 영역의 합: ", sum)
    mean = cv2.mean(frame, mask)
    print("cv2.mean을 이용한 평균: ", mean)

    lst = [0,0,0]
    for i in range(0, 3):
        sum = 0.0
        for j in range(100, 200):
            for k in range(200, 400):
                sum += frame[k][j][i]
        lst[i]=sum/(200*100)
    print("원소 순회를 이용한 평균: ", lst)






    title = "View Frame from Camera"
    cv2.imshow(title, frame)


capture.release()