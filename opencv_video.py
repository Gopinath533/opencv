import cv2


cap = cv2.VideoCapture(0)
vidwrite = cv2.VideoWriter('testvideo.avi', cv2.VideoWriter_fourcc(*'XVID'), 25, (640,480),True)
#out = cv2.VideoWriter('output.avi',fource,20.0,(640,480))
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   #red = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    black= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    vidwrite.write(frame)
    cv2.rectangle(frame,(15,25),(200,150),(0,255,0),5)
    cv2.imshow('frame',frame)
    cv2.imshow('gray', gray)
    #cv2.imshow('red',red)
    cv2.imshow('black',black)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
vidwrite.release()
cv2.destroyAllWindows()