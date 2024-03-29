from multiprocessing import Process
import multiprocessing as mp
from datetime import date, timedelta
import time

def marry(person1, person2, year):
    print("{} married {} in {}".format(person1, person2, year))

def spawn_child(parents):
    gestation = timedelta( days = (9 * 30)).total_seconds()
    time.sleep(gestation)

if __name__ == "__main__":

    NickAndMelissa = Process(target=marry, args=(nick, melissa, 2016))
    NickAndMelissa.start()
    NickAndMelissa.join()

    ctx = mp.get_context('spawn')
    first_child = ctx.Process(target=spawn_child, args=(NickAndMelissa,))
    first_child.start()
    first_child.join() 
    print('WELCOME {}'.format(first_child.name)) #  Output: Mark Whitehill - 2019

    second_child = ctx.Process(target=spawn_child, args=(NickAndMelissa,))
    second_child.start()
    second_child.join()
    print('WELCOME {}'.format(second_child.name)) # Output: Hazel Witehill - 2022
