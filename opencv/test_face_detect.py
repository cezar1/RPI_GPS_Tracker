from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import sys
import numpy as np


cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32


import io
import time
with camera:
    stream = io.BytesIO()
    for f in camera.capture_continuous(stream, format='bgr'):
        stream.truncate()
        stream.seek(0)




        frame=f.array
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)    )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
camera.release()
cv2.destroyAllWindows()
