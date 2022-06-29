#exercise 5-9
#3행 6열의 행렬을 생성하고, 행렬의 원소를 초기화한 후에
#cv2.reduce()함수를 이용해서 가로 방향과 세로 방향으로
#감축하여 평균을 구한 결과를 출력하시오.


import numpy as np
import cv2
M = np.ones((3, 6), np.uint8)

M_ave_column = cv2.reduce(M, dim=0, rtype=cv2.REDUCE_AVG)
M_ave = cv2.reduce(M_ave_column, dim=1, rtype=cv2.REDUCE_AVG)


print (M_ave)