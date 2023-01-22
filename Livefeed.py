# import cv2
from PIL import Image, ImageGrab
from functions import get_runelite
import time
from image_processing import *
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

def start_RL_livefeed_v3(item, frame_num = float('inf'), post_processing = True):

    print_Id()
    start_time = time.time()
    rl = get_runelite("PaulFoster")

    # used to record the time when we processed last frame
    prev_frame_time = 0

    # used to record the time at which we processed current frame
    new_frame_time = 0

    maxframes = frame_num
    frame_count = 0


    with mss() as sct:
        while frame_count < maxframes:
            left, top, width, height, = rl.left, rl.top, rl.width, rl.height
            mon = {'left': left, 'top': top, 'width': width, 'height': height}
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

            # # change img color to RGB - considered for processing
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            if post_processing:

                img, thresh = post_processing_img(img, item = item)
                # targets = image_targets(thresh, img)
                # _ = image_draw(img, targets, draw_all=False)

            # putting the FPS count on the frame
            cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

            cv2.imshow('test', np.array(img))

            if cv2.waitKey(1) & 0xFF in (
                ord('q'),
                27,
            ):
                cv2.destroyAllWindows()
                break


            frame_count += 1

    cv2.destroyAllWindows()
    print(f'total time: {time.time()-start_time}')