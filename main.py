import cv2
import numpy as np

haar_cascade = 'cars.xml'
video = 'Media_analyzed/example_video.mp4'

capture = cv2.VideoCapture(video) 
car_cascade = cv2.CascadeClassifier(haar_cascade)

while True:

    ret, img_frame = capture.read()

    gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.3, 1)

    for (x,y,w,h) in cars: 

        cv2.rectangle(img_frame, (x,y), (x+w,y+h), (0,255,0), 2) 

    cv2.imshow('example_video.mp4', img_frame)

    if cv2.waitKey(33) == 27:
       break

test123 = "testing change"

cv2.destroyAllWindows()