from cv2 import cv2
import numpy as np
import datetime

cap0 = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 255, 0)

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
#assumes same widthxheight for both cams
frame_width = int(cap0.get(3))
frame_height = int(cap0.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out0 = cv2.VideoWriter('outpyTest0.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
out1 = cv2.VideoWriter('outpyTest1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):


    status0, img0 = cap0.retrieve(cap0.grab()) #retrieve and grab the frames, improves performance over read()
    status1, img1 = cap1.retrieve(cap1.grab())

    fps0 = cap0.get(cv2.CAP_PROP_FPS)
    fps1 = cap1.get(cv2.CAP_PROP_FPS)

    cv2.putText(img0, "FPS: {}".format(fps0), (15, 40), font, 1.0, color)
    cv2.putText(img1, "FPS: {}".format(fps1), (15, 40), font, 1.0, color)

    cv2.putText(img0, "Time: {}".format(datetime.datetime.now()), (15, 80), font, 1.0, color)
    cv2.putText(img1, "Time: {}".format(datetime.datetime.now()), (15, 80), font, 1.0, color)

    cv2.imshow("Video0", img0)
    cv2.imshow("Video1", img1)
    out0.write(img0)
    out1.write(img1)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap0.release()
cap1.release()
out0.release()
out1.release()
cv2.destroyAllWindows()
