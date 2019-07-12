import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\Saad\\Desktop\\image project\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("C:\\Users\\Saad\\Desktop\\image project\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml")

img = cv2.imread("face3.jpg",1)


#
# resize = cv2.resize(img,(800,800))

print(img)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
# eyes = eye_cascade.detectMultiScale(gray_img, 1.3, 5 )

print(type(faces))

print(faces)

for x,y,w,h in faces :
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

# for a,b,c,d in eyes :
#     img = cv2.rectangle(img, (a,b), (a+w,b+h), (20,245,0), 3)

cv2.imshow("ASUS",img)
cv2.waitKey(0)
cv2.destroyAllWindows()