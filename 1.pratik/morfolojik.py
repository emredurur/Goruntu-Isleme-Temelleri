import cv2
import numpy as np

image= cv2.imread("engineer.png")

kernel = np.ones((5,5),np.uint8)


erosion = cv2.erode(image,kernel,iterations=1) #  önce aşındırma
dilation = cv2.dilate(erosion,kernel,iterations=1) # sonra genişletme ve temiz gürültüsüz bir resim


cv2.imshow("original",image)

#cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)


cv2.waitKey(0)
cv2.destroyAllWindows()

