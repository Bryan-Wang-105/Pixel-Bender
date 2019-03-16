# Authors: Wang & Johnson Inc. ™
# Usage Notes:
#      Uses OPENCV to capture movement from human motion and animate after-effects using 
#      captured motion
#      https://www.youtube.com/watch?v=nRt2LPRz704&list=WL&index=22&t=0s

# Imports necessary packages
import numpy as np
import cv2
import time

# caps is the mp4 object
capture = cv2.VideoCapture(0)

# create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()


# sets first_frame equal to initial frame in mp4 object
_, first_frame = capture.read()

# Runs for 30 seconds
t_end = time.time() + 60

while time.time() < t_end:
    # sets frame equal to this loop iteration's frame in the mp4
    _, frame = capture.read()

    fgmask = fgbg.apply(frame)

    diff = cv2.absdiff(first_frame,frame)

    # displays feeds
    #cv2.imshow("Standard", frame)
    cv2.imshow("Differences", diff)
    cv2.imshow("Bkgrnd-Rmvl", fgmask)

    first_frame = frame

    key = cv2.waitKey(30)  #if key == 27:#    break

capture.release()
cv2.destroyAllWindows()
