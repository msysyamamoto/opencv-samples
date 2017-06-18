# coding:utf-8
import cv2

cap = cv2.VideoCapture(0)
cascade_path = "../opencv/data/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_path)

over_imgae_path = "./over.png"
over_image = cv2.imread(over_imgae_path, cv2.IMREAD_UNCHANGED)

mask = over_image[:,:,3]  # extract alpha channel
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
over_image = cv2.imread(over_imgae_path) # no alpha

_response, frame = cap.read()
minsize = (int(frame.shape[0] * 0.1), int(frame.shape[1] * 0.1))

while True:
    _response, frame = cap.read()
    facerect = cascade.detectMultiScale(frame, scaleFactor=1.11, minNeighbors=3, minSize=minsize)

    for rect in facerect:
        x, y, w, h = rect
        oi = cv2.resize(over_image, (w, h))
        rmask = cv2.resize(mask, (w, h))
        rmask = rmask <= 1

        frame[y:y+h, x:x+w] *= rmask
        frame[y:y+h, x:x+w] += oi

    key = cv2.waitKey(1)
    if key == ord("\r"):
        cv2.imwrite("./camera.png", frame)
        print("save picture.")
        frame[:] = 255 # flash effect

    cv2.imshow("face camera", frame)
