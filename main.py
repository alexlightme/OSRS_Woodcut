
from alexosrs_functions import *
from Livefeed import *
from functions import get_runelite
from multiprocessing import Process
from multiprocess_funcs import *




def main():

    print('main fun')
    print('process id:', os.getpid())


    dimensions = get_runelite_dimensions("PaulFoster")
    rl = get_runelite("PaulFoster")
    left_x = dimensions[0].x
    top_y = dimensions[2].y
    right_x = dimensions[1].x
    bottom_y = dimensions[0].y


    # p1 = Process(target=kill_tags)
    # p1.start()

    p2 = Process(target=start_RL_livefeed_v3, args=(rl.left,rl.top, rl.width, rl.height))
    p2.start()
    # p1.join()
    p2.join()


if __name__=="__main__":

    main()



