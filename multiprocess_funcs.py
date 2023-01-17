import os


def print_Id():

    print('--------------------------')

    print('calling fun')
    print('parent process id:', os.getppid())
    print('process id:', os.getpid())



