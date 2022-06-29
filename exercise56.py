#exercise 5-6
#다음 예시 코드는 컴파일 에러가 발생한다.
#에러가 발생하는 부분을 수정하고 실행 결과를 적으시오.

import numpy as np, cv2

m1 = np.array([1, 2, 3, 1, 2, 3])
m2 = np.array([3, 3, 4, 2, 2, 3])
m3 = m1 + m2
m4 = m1 - m2

print("[m1] = %s" %m1)
print("[m2] = %s" %m2)
print("[m3] = %s" %m3)
print("[m4] = %s" %m4)