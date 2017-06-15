# coding:utf-8
import cv2

cap = cv2.VideoCapture(0)
cascade_path = "../opencv/data/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)

over_imgae_path = "./over.png"
# over_image = cv2.imread(over_imgae_path, cv2.IMREAD_UNCHANGED) 
over_image = cv2.imread(over_imgae_path) # without alpha channel

color = (0, 255, 0)
_response, frame = cap.read()
minsize = (int(frame.shape[0] * 0.1), int(frame.shape[1] * 0.1))

while True:
    _response, frame = cap.read()
    facerect = cascade.detectMultiScale(frame, scaleFactor=1.11, minNeighbors=3, minSize=minsize)

    for rect in facerect:
        x, y, w, h = rect
        oi = cv2.resize(over_image, (w, h))
        frame[y:y+h, x:x+w] = oi

    cv2.waitKey(1)
    cv2.imshow("face camera", frame)
