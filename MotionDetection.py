import cv2

#cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture(
    '/home/shanto/Downloads/vlc-record-2020-03-05-11h12m07s-rtsp___192.168.107.241_554_cam_realmonitor-.mp4')


ret, frame1 = cap.read()
ret, frame2 = cap.read()

ahead=0

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)>1500:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            ahead=20
    ahead=ahead-1
    print(ahead)
    if ahead!=0:
        cv2.putText(frame1, "Status : {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)
    else:
        print("---------------->")

    cv2.imshow("Feed", frame1)
    frame1 = frame2
    ret,frame2 = cap.read()
    #print(frame1)
    #print(frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
