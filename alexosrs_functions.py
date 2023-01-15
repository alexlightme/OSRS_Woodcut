from functions import Image_count
from functions import image_Rec_clicker
from functions import release_drop_item
from functions import drop_item
from functions import random_breaks
from functions import find_Object
from functions import get_runelite_dimensions
from functions import get_runelite


def drop_icon(icon):
    j = 0
    invent = Image_count(icon)
    print(invent)

    dimensions = get_runelite_dimensions("PaulFoster")
    left_x = dimensions[0].x
    top_y = dimensions[2].y
    right_x = dimensions[1].x
    bottom_y = dimensions[0].y

    if invent > 20:
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



        find_Object(2,left_x, top_y, right_x, bottom_y)
        random_breaks(30, 15)

def kill_tags():
    j = 0
    while j<10:
        dimensions = get_runelite_dimensions("PaulFoster")
        left_x = dimensions[0].x
        top_y = dimensions[2].y
        right_x = dimensions[1].x
        bottom_y = dimensions[0].y

        find_Object(5,left_x, top_y, right_x, bottom_y)
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



