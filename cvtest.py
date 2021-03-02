import cv2
import numpy as np

cap = cv2.VideoCapture('WhatsApp Video 2021-03-01 at 13.37.13.mp4')
cap2 = cv2.VideoCapture('WhatsApp Video 2021-03-01 at 13.37.13.mp4')
while(True):
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    cv2.imshow('frame', frame)
    cv2.imshow('frame2', frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()