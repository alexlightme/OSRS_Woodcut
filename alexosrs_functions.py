from functions import Image_count
from functions import image_Rec_clicker
from functions import release_drop_item
from functions import drop_item
from functions import random_breaks
# from functions import find_Object
from functions import get_runelite_dimensions, get_runelite
from multiprocess_funcs import *
import pyautogui
import random
from image_processing import *
from PIL import Image, ImageGrab
from mouse_key_funcs import move_and_click
from functions import get_runelite
from mss import mss




def drop_icon(icon):
    j = 0

    while True:
        invent = Image_count(icon)
        print(invent)
        rl = get_runelite("PaulFoster")
        dimensions = get_runelite_dimensions("PaulFoster")
        left_x = dimensions[0].x
        top_y = dimensions[2].y
        right_x = dimensions[1].x
        bottom_y = dimensions[0].y

        if invent > 20:
            random_breaks(5,10)
            rl.activate()
            drop_item()
            image_Rec_clicker(icon, 'item', 5, 5, 0.9,'left', left=left_x, top=top_y, right=right_x, bottom=bottom_y)
            release_drop_item()

def get_wood():
    j = 0
    while j<10:
        drop_icon("wood_icon.png")
        dimensions = get_runelite_dimensions("PaulFoster")
        left_x = dimensions[0].x
        top_y = dimensions[2].y
        right_x = dimensions[1].x
        bottom_y = dimensions[0].y

        rl = get_runelite("PaulFoster")

        left, top, width, height, = rl.left, rl.top, rl.width, rl.height
        mon = {'left': left, 'top': top, 'width': width, 'height': height}

        with mss() as sct:

            screenShot = sct.grab(mon)
            img = Image.frombytes(
                'RGB',
                (screenShot.width, screenShot.height),
                screenShot.rgb,
            )

        # change img color to RGB - considered for processing
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        img_coordinates = find_Object(img, 2)
        img_coordinates[0] = img_coordinates[0] + left_x
        img_coordinates[1] = img_coordinates[1] + top_y

        if img_coordinates:
            move_and_click(img_coordinates)
        random_breaks(30, 15)

def kill_tags():
    j = 0
    print_Id()
    while j<10:
        dimensions = get_runelite_dimensions("PaulFoster")
        left_x = dimensions[0].x
        top_y = dimensions[2].y
        right_x = dimensions[1].x
        bottom_y = dimensions[0].y

        mouse_coords = find_Object(5,left_x, top_y, right_x, bottom_y)
        b = random.uniform(0.1, 0.2)
        pyautogui.moveTo(mouse_coords[0], mouse_coords[1], duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)

        random_breaks(20, 15)


def fish_shrimp():
    j = 0
    while j<10:

        invent = Image_count('shrimp_icon.png')
        print(invent)

        dimensions = get_runelite_dimensions("PaulFoster")
        left_x = dimensions[0].x
        top_y = dimensions[2].y
        right_x = dimensions[1].x
        bottom_y = dimensions[0].y

        find_Object(6,left_x, top_y, right_x, bottom_y)
        random_breaks(40, 15)

        if invent > 11:
            drop_item()
            image_Rec_clicker('shrimp_icon.png', 'item', 5, 5, 0.9,'left', left=left_x, top=top_y, right=right_x, bottom=bottom_y)
            release_drop_item()



