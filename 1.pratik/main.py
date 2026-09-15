import cv2

from pathlib import Path



image = cv2.imread("images/araba.jpg")


if image is None:
    print("fotoğraf okunamadı")
else:
    
    print("original",image.shape) # (450, 750, 3)
    gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    

    resize = cv2.resize(image, (600,600))
    
    print("resize:",resize.shape)

    gaussian = cv2.GaussianBlur(gray, (3,3), 0)
    

    ret, thresh= cv2.threshold(gaussian,127,255,cv2.THRESH_BINARY)

    ret, otsu = cv2.threshold(gaussian,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    


    cv2.imshow("original",image)
    cv2.imshow("gray",gray)
    cv2.imshow("resize",resize)
    cv2.imshow("gaussin",gaussian)
    cv2.imshow("thresh",thresh)
    cv2.imshow("otsu", otsu)

    print("OTSU'nun sectigi esik:", ret)

    output_dir = Path("outputs")

    if not output_dir.exists():
        output_dir.mkdir()
      
    outputs = {

            "original.jpg":image,
            "gray.jpg":gray,
            "resize.jpg":resize,
            "gaussin.jpg":gaussian,
            "thresh.jpg":thresh,
            "otsu.jpg":otsu

        }

    for name,img in outputs.items():
        cv2.imwrite(f"outputs/{name}",img)


    cv2.waitKey(0)
    cv2.destroyAllWindows()


