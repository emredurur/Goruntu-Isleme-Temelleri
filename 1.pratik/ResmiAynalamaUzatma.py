import cv2
import numpy as np

resim = cv2.imread("images/kemalSunal.png")

aynalananResim = cv2.copyMakeBorder(resim,200,200,300,325,cv2.BORDER_REFLECT)
uzatılanResim = cv2.copyMakeBorder(resim,100,200,150,40,cv2.BORDER_REPLICATE)
tekrarResim = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_WRAP)
sarilanResim = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=(200,132,165))



cv2.imshow("Aynalanmıs Resim",aynalananResim)
cv2.imshow("Uzatilan Resim",uzatılanResim)
cv2.imshow("tekrar Resim",tekrarResim)
cv2.imshow("sarilan Resim",sarilanResim)



cv2.waitKey(0)
cv2.destroyAllWindows()

