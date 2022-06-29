#영상처리에서 투영은 다음의 수식으로 표현된다.
#OpenCV함수 중에 cv2.reduce() 함수를 이용해서 수식과 같이
#수직 및 수평 방향 투영을 수행하는 프로그램을 작성하기고,
#영상 파일을 읽어서 투영 히스토그램을 출력하시오.

import numpy as np, cv2

image = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception ("ERROR: Reading image")
image = np.float32(image)

histo_row= cv2.reduce (image, dim=0, rtype = cv2.REDUCE_SUM)
histo_col = cv2.reduce (image, dim=1, rtype = cv2.REDUCE_SUM)
histo_row= histo_row.flatten()
histo_col= histo_col.flatten()

def draw_hist (hist):
    shape = (200, 256)
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)
    gap = hist_img.shape[1]/hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i*gap))
        w = int(round(gap))
        cv2.rectangle (hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0)


hist_row_img = draw_hist(histo_row)
hist_col_img = draw_hist(histo_col)
cv2.imshow("hist_row_img", hist_row_img)
cv2.imshow("hist_col_img", hist_col_img)
cv2.waitKey(0)


