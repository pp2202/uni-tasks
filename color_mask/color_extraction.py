import cv2 as cv
import numpy as np

def color_treshhold(a):

    background_removal = cv.createBackgroundSubtractorMOG2()
    cap = cv.VideoCapture(a)

    kernel_o = np.ones((9,9),np.uint8)
    kernel_c = np.ones((12,12),np.uint8)

    frame_width = int(cap.get(3)*0.2)
    frame_height = int(cap.get(4)*0.2)

    dims = (frame_width,frame_height)

    out = cv.VideoWriter('th output preview 2.avi',cv.VideoWriter_fourcc('M','J','P','G'), 50, (frame_width,frame_height))

    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    while(True):
        ret, frame = cap.read()

        if ret == True:
           
            bg_rem_mask = background_removal.apply(frame)
            
            frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            
            th_frame = frame.copy()

            lower_red_mask = np.array([0,180,30])
            
            upper_red_mask = np.array([7,255,255])
            
            lower_blue_mask = np.array([100,160,30])
            
            upper_blue_mask = np.array([120,255,255])

            lower_red_mask_upper_hue = np.array([172,120,30])

            upper_red_mask_upper_hue = np.array([179,255,255])
            
            red_mask = cv.inRange(frame, lower_red_mask, upper_red_mask)
            
            blue_mask = cv.inRange(frame, lower_blue_mask, upper_blue_mask)

            upper_hue_red_mask = cv.inRange(frame, lower_red_mask_upper_hue, upper_red_mask_upper_hue)
            
            th_frame = cv.bitwise_and(th_frame, th_frame, mask=(blue_mask|red_mask|upper_hue_red_mask)&bg_rem_mask)

            rgb_frame = cv.cvtColor(th_frame, cv.COLOR_HSV2BGR)

            cleanedup_frame = cv.morphologyEx(cv.morphologyEx(rgb_frame, cv.MORPH_OPEN, kernel_o), cv.MORPH_CLOSE, kernel_c)

            resized_frame = cv.resize(cleanedup_frame, dims, interpolation=cv.INTER_CUBIC)

            out.write(resized_frame)


        else:
            break

    cap.release()
    out.release()



color_treshhold("one round kam4.mp4")
                

