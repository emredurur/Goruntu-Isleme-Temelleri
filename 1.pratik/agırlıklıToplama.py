import cv2
import numpy as np


resim1 = cv2.imread("images/Cem_Yilmaz.png")
resim2 = cv2.imread("images/Ozan_Guven.png")


resim2 = cv2.resize(resim2,(1232,1098))


toplam = cv2.add(resim1,resim2)
agirlikliToplam = cv2.addWeighted(resim1,0.7,resim2,0.3,0)


cv2.imshow("Cem Yılmaz",resim1)
cv2.imshow("Ozan Güven",resim2)
cv2.imshow("toplanmis resimler",toplam)
cv2.imshow("agirlikli toplanmis resimler",agirlikliToplam)

cv2.waitKey(0)
cv2.destroyAllWindows()