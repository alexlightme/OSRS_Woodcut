


import numpy as np
import cv2
from PIL import Image, ImageGrab


def color_change(image, item):

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([150, 0, 100], [255, 60, 160])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    green_tag = ([240, 230, 0], [255, 255, 0])  # 5 Index
    shrimp_tag = ([205, 205, 0], [205, 205, 0])  # 6 Index

    object_list = [red, green, amber, pickup_high, attack_blue, green_tag, shrimp_tag]
    boundaries = [object_list[item]]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(np.array(image), lower, upper)
        output = cv2.bitwise_and(np.array(image), np.array(image), mask=mask)

    return output






