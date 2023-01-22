
from alexosrs_functions import *
from Livefeed import start_RL_livefeed_v3
from multiprocessing import Process
from multiprocess_funcs import *
import cProfile
# import profile

# profiling function ------ cProfile.runctx('start_RL_livefeed_v3()', globals(), locals())
import pstats

def main():

    print('main fun')
    print('process id:', os.getpid())


    # p1 = Process(target=kill_tags)
    # p1.start()
    # get_wood()
    start_RL_livefeed_v3(10, post_processing=False)
    # drop_icon("salmon_icon.png")

    # p2 = Process(target=start_RL_livefeed_v3, args=(False, ))
    # p2.start()
    # p1.join()
    # p2.join()


if __name__=="__main__":

    main()



