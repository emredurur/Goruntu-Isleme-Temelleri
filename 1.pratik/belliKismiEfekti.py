import cv2 
import numpy as np

resim = cv2.imread("kemalSunal.png")

resim[250:350,570:850,2] = 255
resim[250:350,570:850,1] = 32
resim[250:350,570:850,0] = 124 


cv2.imshow("kemal sunal fotosu: ", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()