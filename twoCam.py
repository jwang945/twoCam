from cv2 import cv2
import numpy as np

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)


# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
#assumes same widthxheight for both cams
frame_width = int(cap0.get(3))
frame_height = int(cap0.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out0 = cv2.VideoWriter('outpyTest0.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
out1 = cv2.VideoWriter('outpyTest1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
    # Capture frame-by-frame
    ret0, frame0 = cap0.read()
    ret1, frame1 = cap1.read()
    # Our operations on the frame come here
    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame0',gray0)
    cv2.imshow('frame1',gray1)

    if ret0 == True:
        out0.write(frame0)
    if ret1 == True:
        out1.write(frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap0.release()
cap1.release()
out0.release()
out1.release()
cv2.destroyAllWindows()