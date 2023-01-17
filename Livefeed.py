import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageGrab
from functions import get_runelite
import time
from image_processing import *
from Scrap_functions import *
from multiprocess_funcs import *
from scipy.spatial import distance
import numpy as np
from mss import mss


def fps_calc(newframe_t, prevframe_t):

    fps = 1/(newframe_t -prevframe_t)
    return fps



def screen_Image_capture(left=0, top=0, right=0, bottom=0):
    if left != 0 or top != 0 or right != 0 or bottom != 0:
        myScreenshot = ImageGrab.grab(bbox=(left, top, right, bottom),all_screens=True)
    else:
        myScreenshot = ImageGrab.grab(all_screens=True)
    return myScreenshot


def start_RL_livefeed_v3(left, top, width, height, post_processing = True):

    print_Id()

    mon = {'left': left, 'top': top, 'width': width, 'height': height}

    # used to record the time when we processed last frame
    prev_frame_time = 0

    # used to record the time at which we processed current frame
    new_frame_time = 0
    kernel = np.ones((2,2), np.uint8)


    with mss() as sct:
        while True:
            screenShot = sct.grab(mon)
            img = Image.frombytes(
                'RGB',
                (screenShot.width, screenShot.height),
                screenShot.rgb,
            )

            # fps calculations before frame is adjusted
            new_frame_time = time.time()
            fps = fps_calc(new_frame_time, prev_frame_time)
            prev_frame_time = new_frame_time
            font = cv2.FONT_HERSHEY_SIMPLEX
            fps = int(fps)
            # converting the fps to string so that we can display it on frame
            # by using putText function
            fps = str(fps)

            rgb_bounds = ([0, 0, 0], [255, 255, 255])

            # change img color to RGB - considered for processing
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
            if post_processing:
                image_center = np.asarray(img_gray.shape) / 2
                # Reversed tuple so coordinates can be found as x, y
                image_center = tuple(image_center.astype('int32'))[::-1]

                # apply on image
                cv2.circle(img, image_center, 30, (255, 100, 0), 4)
                cv2.rectangle(img, pt1=(1100, 0), pt2=(1400, 200), color=(0, 0, 0), thickness=-1)



                # remove colors from image
                mask = color_mask(img, 5)

                ret, thresh = cv2.threshold(mask, 40, 255, cv2.THRESH_BINARY)
                # Pumps up the lines --- IDK how this actually works but makes colors thick
                thresh = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
                # Finds contours between where the binary is white
                contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


                # output = cv2.bitwise_and(img, img)

                # Find features/Objects from contours
                if len(contours) != 0:

                    rects = []
                    for c in contours:
                        # find center of each contour
                        M = cv2.moments(c)
                        center_X = int(M["m10"] / M["m00"])
                        center_Y = int(M["m01"] / M["m00"])
                        contour_center = (center_X, center_Y)

                        # calculate distance to image_center
                        distances_to_center = (distance.euclidean(image_center, contour_center))

                        # save to a list of dictionaries
                        rects.append(
                            {'contour': c, 'center': contour_center, 'distance_to_center': distances_to_center})

                    targets = sorted(rects, key=lambda i: i['distance_to_center'])
                    x, y, w, h = cv2.boundingRect(targets[0]['contour'])

                    # Draw based on contours
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

            # putting the FPS count on the frame
            cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

            cv2.imshow('test', np.array(img))
            if cv2.waitKey(33) & 0xFF in (
                ord('q'),
                27,
            ):
                cv2.destroyAllWindows()
                break