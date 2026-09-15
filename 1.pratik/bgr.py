import cv2
import numpy as np

resim = cv2.imread("groott.png")

resim[30,40]=[0,0,255]
y=0 
for i in range(500):
    
    resim[30,40+i] = [0,0,255]

    for y in range(500):
        resim[30+y,40+i] = [0,0,255]
        y = y + 1 
     



cv2.imshow("resim",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()