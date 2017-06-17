# coding:utf-8
import cv2

cap = cv2.VideoCapture(0)
cascade_path = "../opencv/data/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)

_response, frame = cap.read()
minsize = (int(frame.shape[0] * 0.08), int(frame.shape[1] * 0.08))

while True:
    _response, frame = cap.read()
    facerect = cascade.detectMultiScale(frame, scaleFactor=1.11, minNeighbors=3, minSize=minsize)

    rect_count = len(facerect)

    if rect_count >= 2:
        halv_count = int(rect_count/2)
        rfacerect = facerect[::-1]
        facerect  = facerect[:halv_count]
        rfacerect = rfacerect[:halv_count]

        for (rect1, rect2) in zip(facerect, rfacerect):
            x1, y1, w1, h1 = rect1
            x2, y2, w2, h2 = rect2

            face1 = frame[y1:y1+h1, x1:x1+w1]
            face2 = frame[y2:y2+h2, x2:x2+w2]

            face1 = cv2.resize(face1, (w2, h2))
            face2 = cv2.resize(face2, (w1, h1))

            frame[y1:y1+h1, x1:x1+w1] = face2
            frame[y2:y2+h2, x2:x2+w2] = face1

    cv2.waitKey(1)
    cv2.imshow("face camera", frame)
