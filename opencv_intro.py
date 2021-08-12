import cv2
# import matplotlib.plyplot as plt
import numpy as np

img = cv2.imread("./image/a.jpg")
print(img)

# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow("gopi",img)
cv2.waitKey(0)
#cv2.destroyAllWindows()