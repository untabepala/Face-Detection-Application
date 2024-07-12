import cv2

face=cv2.CascadeClassifier("open/haarcascade_frontalface_default.xml")

img=cv2.imread("open/mine.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
detect=face.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in detect:
    cv2.rectangle(img,(x,y),(x+w , y+h),(255,0,0),2)



cv2.imshow("faceDetect",img)
cv2.waitKey(0)