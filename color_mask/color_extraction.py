import cv2 as cv
import numpy as np

def color_treshhold(a):

    background_removal = cv.createBackgroundSubtractorMOG2()
    cap = cv.VideoCapture(a)

    #pre-made kernels for the morphological noise removal
    kernel_o = np.ones((9,9),np.uint8)
    kernel_c = np.ones((12,12),np.uint8)

    #importing the frame dimensions and rescaling them for the output
    frame_width = int(cap.get(3)*0.4)
    frame_height = int(cap.get(4)*0.4)
    dims = (frame_width,frame_height)

    #declaring output file
    out = cv.VideoWriter('th output preview 2.avi',cv.VideoWriter_fourcc('M','J','P','G'), 50, dims)

    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    while(True):
        ret, frame = cap.read()

        if ret == True:
            #creating a mask for removing the background using the frame with rgb data
            bg_rem_mask = background_removal.apply(frame)
            
            frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            #creating a snapshot of the frame to allow for masking later on            
            th_frame = frame.copy()

            #creating ranges for the HSV masks and merging them
            lower_red_mask = np.array([0,180,30])
            upper_red_mask = np.array([7,255,255])
            
            lower_blue_mask = np.array([100,160,30])
            upper_blue_mask = np.array([120,255,255])

            lower_red_mask_upper_hue = np.array([172,120,30])
            upper_red_mask_upper_hue = np.array([179,255,255])
            
            red_mask = cv.inRange(frame, lower_red_mask, upper_red_mask)        
            blue_mask = cv.inRange(frame, lower_blue_mask, upper_blue_mask)
            upper_hue_red_mask = cv.inRange(frame, lower_red_mask_upper_hue, upper_red_mask_upper_hue)
            

            #applying all the created masks to the existing copy of our frame
            th_frame = cv.bitwise_and(th_frame, th_frame, mask=(blue_mask|red_mask|upper_hue_red_mask)&bg_rem_mask)
            #conversion back to rgb colour space
            rgb_frame = cv.cvtColor(th_frame, cv.COLOR_HSV2BGR)
            #removing noise from the frame using morphology 
            cleanedup_frame = cv.morphologyEx(cv.morphologyEx(rgb_frame, cv.MORPH_OPEN, kernel_o), cv.MORPH_CLOSE, kernel_c)
            #resizing the frame to the converted video's size
            resized_frame = cv.resize(cleanedup_frame, dims, interpolation=cv.INTER_CUBIC)

            out.write(resized_frame)


        else:
            break

    cap.release()
    out.release()



color_treshhold("one round kam4.mp4")
                

