import cv2
import numpy as np
face_cas = cv2.CascadeClassifier('./image/haarcascade_frontalface_default.xml')
eye_cas = cv2.CascadeClassifier('./image/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        #cv2.rectangle(img,start_point,end_point,color,thickness)
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+h]
        eye = eye_cas.detectMultiScale(roi_gray)
        for (xe,ye,we,he) in eye:
            cv2.rectangle(roi_color,(xe,ye),(xe+we,ye+he),(0,255,0),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()