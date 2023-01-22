
import numpy as np
import cv2
from scipy.spatial import distance
import random

kernel = np.ones((2, 2), np.uint8)


def color_mask(image, item):

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([150, 0, 100], [255, 60, 160])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    green_tag = ([240, 230, 0], [255, 255, 0])  # 5 Index
    shrimp_tag = ([205, 205, 0], [205, 205, 0])  # 6 Index
    road_tag = ([71*.9, 72*.9, 79*.9], [71*1.1, 72*1.1, 79*1.1])  # 7 Index
    black_tag = ([0, 0, 0], [1, 1, 1])  # 8 Index
    water_tag = ([0, 0, 255], [255, 255, 255])  # 9 Index
    bright_tag = ([180, 180, 180], [255, 255, 255])  # 10 Index


    object_list = [red, green, amber, pickup_high, attack_blue, green_tag, shrimp_tag, road_tag, black_tag,water_tag, bright_tag]
    lower, upper = object_list[item][0], object_list[item][1]

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(np.array(image), lower, upper)
    return mask



def post_processing_img(img, item = 5):
    """
    Processes image, and outputs various versions of the processed image
    :param img:
    :return:
    """

    img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    image_center = np.asarray(img_gray.shape) / 2
    # Reversed tuple so coordinates can be found as x, y
    image_center = tuple(image_center.astype('int32'))[::-1]

    # apply on image before calcs
    # cv2.rectangle(img, pt1=(1100, 0), pt2=(1400, 200), color=(0, 0, 0), thickness=-1)

    # remove colors from image
    mask = color_mask(img, item)
    # ## final mask and masked
    # mask = cv2.bitwise_or(mask1, mask2)
    # target = cv2.bitwise_and(img, img, mask=mask)

    ret, thresh = cv2.threshold(mask, 40, 255, cv2.THRESH_BINARY)
    # removes the fill and trys to capture the perimeter
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)


    # apply on image after calcs
    cv2.circle(img, image_center, 10, (255, 100, 0), 4)

    return img, thresh

def image_targets(thresh, img):
    # Finds contours between where the binary is white

    img_gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    image_center = np.asarray(img_gray.shape) / 2

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
    return targets

def image_draw(img, targets, draw_all = False) -> list:

    if draw_all:
        for target in targets:
            x, y, w, h = cv2.boundingRect(target['contour'])

            # Draw calcs based on contours
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    else:
        x, y, w, h = cv2.boundingRect(targets[0]['contour'])

        # Draw calcs based on contours
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    return [x, y, w, h]

def find_Object(image, item, left=0, top=0):
    img, thresh = post_processing_img(image, item)
    x, y, w, h = image_targets(thresh, img)
    if x:
        assert w > 30, "rect too small"
        print((x + 15, x + w - 15))
        x = random.randrange(x + 15, x + w - 15)  # 950,960
        # print('x: ', x)
        print((y + 15, y + w - 15))
        y = random.randrange(y + 15, y + h - 15)  # 490,500
        # print('y: ', y)
        return (x, y)
    else:
        return None



def show_cv2_image(img):
    cv2.imshow('test', np.array(img))

    if cv2.waitKey(1) & 0xFF in (
            ord('q'),
            27,
    ):
        cv2.destroyAllWindows()
    return

