import cv2 
import numpy as np

resim = cv2.imread("cocuk.png")


kesit = resim[200:300,500:670]

kesit[:,:,2]=255

resim[0:100,0:170] = kesit


cv2.imshow("foto:", resim)
cv2. imshow("kesit: ", kesit)

cv2.waitKey(0)
cv2.destroyAllWindows()