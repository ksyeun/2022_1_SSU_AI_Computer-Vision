import numpy as np, cv2, pickle
def findCorners(image, bSize):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, bSize) # 코너 검출

    if ret:        # 부화소(subpixel) 위치를 찾아서 코너 좌표 개선
        criteria = (cv2.TermCriteria_MAX_ITER + cv2.TermCriteria_EPS, 30, 0.1)
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    return ret, np.array(corners, np.float32), image

def show_image(file, bSize, result):
    cv2.drawChessboardCorners(result[2], bSize, result[1], result[0])  # 코너 표시
    cv2.imshow(file, result[2])

def calibrate_correct(objectPoints, imagePoints, image):
    size = image.shape[1::-1]
    ret = cv2.calibrateCamera(objectPoints, imagePoints, size, None, None)

    newSacle, roi = cv2.getOptimalNewCameraMatrix(ret[1], ret[2], size, 1)
    undistorted = cv2.undistort(image, ret[1], ret[2], None, newSacle)
    x, y, w, h = roi
    return ret, undistorted, undistorted[y:y + h, x:x + w]  # 왜곡 영역 제거

def put_string(frame, text, pt, value=None, color=(120, 200, 90)) :
    text = str(text) + str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2) # 그림자 효과
    cv2.putText(frame, text, pt   , font, 0.7, color, 2) # 작성 문자

bSize, mode = (8,7), 'detect mode'             # 체스판 코너수, 카메라 모드
imagePoints= []                                 # 영상 코너 좌표
points = [(x, y, 0) for y in range(bSize[1]) for x in range(bSize[0])]
points = np.array(points, np.float32)

capture = cv2.VideoCapture(0)
if capture.isOpened() is False: raise Exception('카메라 연결 안됨')
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)
print('카메라 연결 완료')

while(True):
    ret, frame = capture.read()
    key = cv2.waitKey(30)
    if key == 27 or ret is False : break     #  esc 키이면 종료
    if key == 13: mode = 'correct mode'      # 엔터키
    if key == 8:  mode = 'detect mode'       # 백페이스바키

    if mode =='detect mode':
        ret, corners, img = findCorners(frame, bSize)    # 코너 검출
        if ret: show_image('image', bSize, (ret, corners, img))

        if ret and key == 32:                      # 스페이스바이면 저장
            imagePoints.append(corners)             # 코너 좌표 저장
            put_string(frame, "save cord: ", (10, 40), len(imagePoints) )
            cv2.imshow("image", frame)
            cv2.waitKey(500)                        # 표시 내용 보이기 위해 잠깐 멈춤
        else:
            put_string(frame, mode, (10, 40), '')
            cv2.imshow("image", frame)

    elif mode == 'correct mode':
        if len(imagePoints) >= 3 :
            objectPoints = [points] * len(imagePoints)
            ret, undistored, correct_img = calibrate_correct(objectPoints, imagePoints, frame)
            file = open('pickle_example.pickle', 'wb')
            data = undistored
            pickle.dump(data, file)
            put_string(frame, mode, (400, 40), '')
            cv2.imshow('image', frame)
        else:
            put_string(frame, "Capture more than 3 corner coordinates", (70, 200))
            cv2.imshow("image", frame)
            cv2.waitKey(1000)
            mode = 'detect mode'
file.close()
capture.release()
