# coding:utf-8
import cv2

cap = cv2.VideoCapture(0)
cascade_path = "./haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)

color = (0, 255, 0)
_response, frame = cap.read()
minsize = (int(frame.shape[0] * 0.1), int(frame.shape[1] * 0.1))

while True:
    _response, frame = cap.read()
    facerect = cascade.detectMultiScale(frame, scaleFactor=1.11, minNeighbors=3, minSize=minsize)

    for rect in facerect:
        x, y , w, h = rect
        # print(x, y, x + w, y + h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    cv2.waitKey(1)
    cv2.imshow("face camera", frame)
