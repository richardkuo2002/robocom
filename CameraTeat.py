import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')
cap = cv2.VideoCapture(0)

plt.ion()
while cap.isOpened():
    
    time.sleep(.05)
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        plt.imshow(frame)
        plt.pause(.01)
        plt.cla()  # clear axis
        plt.clf()

    if cv2.waitKey(1) ==13: #13 is the Enter Key
        break
        
plt.ioff()
cap.release()
cv2.destroyAllWindows()