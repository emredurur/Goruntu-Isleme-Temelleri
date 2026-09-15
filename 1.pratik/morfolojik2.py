import cv2
import numpy as np



image= cv2.imread("images/engineer.png")

kernel = np.ones((5,5),np.uint8)


opening= cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel) # önce aşındırma sonra genişletme

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE,kernel) # önce genişlet sonra aşındır

gradyan = cv2.morphologyEx(image , cv2.MORPH_GRADIENT,kernel) # dilation (genişletme) - erosion(aşındırma)


cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradyan",gradyan)


cv2.waitKey(0)
cv2.destroyAllWindows()