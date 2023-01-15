
from alexosrs_functions import *
from threading import Thread
from Livefeed import *
from functions import get_runelite




if __name__=="__main__":


    dimensions = get_runelite_dimensions("PaulFoster")
    rl = get_runelite("PaulFoster")
    left_x = dimensions[0].x
    top_y = dimensions[2].y
    right_x = dimensions[1].x
    bottom_y = dimensions[0].y

    # get_wood()

    start_RL_livefeed_v3(rl.left,rl.top, rl.width, rl.height, post_processing=True)
    # Thread(target = get_wood()).start()
    # Thread(target=start_RL_livefeed()).start()










