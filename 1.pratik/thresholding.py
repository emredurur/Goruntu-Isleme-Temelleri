import cv2

image = cv2.imread("parmakizi.png",0)

#resize=image.resize((500,500))

# SIMPLE THRESHHOLDINGLER
ret, thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
#ret, thresh3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
#ret, thresh4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
#ret, thresh5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)


# adaptive thresholding
adaptive1 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
adaptive2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# otsu thresholding

ret12, thresh12 =cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)



cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
#cv2.imshow("thresh2",thresh2)
#cv2.imshow("thresh3",thresh3)
#cv2.imshow("thresh4",thresh4)
#cv2.imshow("thresh5",thresh5)
cv2.imshow("adaptive1",adaptive1)
cv2.imshow("adaptive2",adaptive2)
cv2.imshow("otsu",thresh12)
cv2.waitKey(0)
cv2.destroyAllWindows()