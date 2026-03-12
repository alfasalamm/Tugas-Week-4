#AKSES IP CAMERA
import cv2
cap = cv2.VideoCapture("http://192.168.1.6:8080//video")
while True:
    ret, frame = cap.read()
    cv2.imshow('IP Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()