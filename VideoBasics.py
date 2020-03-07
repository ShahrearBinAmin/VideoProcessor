import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
#cap=cv2.VideoCapture('/home/shanto/Downloads/vlc-record-2020-03-05-11h12m07s-rtsp___192.168.107.241_554_cam_realmonitor-.mp4')

while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("WebCam", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()