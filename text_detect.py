import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

image: None = cv2.imread('youtube_.png')

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height,width,_ = image.shape

box = pytesseract.image_to_boxes(image)
#print(box)

for b in box.splitlines():
    b = b.split()
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,height-y),(w+10,height-h),(0,255,0),3)
    cv2.putText(image,b[0],(x,height-y),cv2.FONT_ITALIC,1,(0,0,255),1)
cv2.imshow('Output',image)
cv2.waitKey(0)

