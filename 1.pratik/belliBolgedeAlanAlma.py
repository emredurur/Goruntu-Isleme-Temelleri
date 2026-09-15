import cv2
import numpy as np 

resim = cv2.imread("images/cocuk.png")

print(resim.shape)
cv2.rectangle(resim,(600,250),(800,30),[255,0,245],12)


cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
