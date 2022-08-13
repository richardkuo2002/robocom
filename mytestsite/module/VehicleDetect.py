import cv2

# capture frames from a video
cap = cv2.VideoCapture("/Users/richard/Downloads/video.avi")

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('/Users/richard/Desktop/Coding/robocom_html/mytestsite/module/car.xml')

# plt.ion()

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)


    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    # Display frames in a window 
    cv2.imshow('video2', frames)

    #  Windows 要註解這區域{
    # plt.imshow(frames)
    # plt.pause(.01)
    # plt.cla()  # clear axis
    # plt.clf()
    # }
        
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# Window 要註解這一區 {
# cv2.destroyAllWindows()
# plt.ioff()
# }

cap.release()
# De-allocate any associated memory usage
# cv2.destroyAllWindows()