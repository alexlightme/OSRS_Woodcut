





import random
import pyautogui



def move_and_click(img_coordinates):
    b = random.uniform(0.1, 0.2)
    pyautogui.moveTo(img_coordinates[0], img_coordinates[1], duration=b)
    b = random.uniform(0.01, 0.05)
    pyautogui.click(duration=b)

    return None
























