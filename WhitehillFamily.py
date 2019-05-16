from multiprocessing import Process
from datetime import date, timedelta

def attend_CSU(name, year):
    print("{} attended CSU in {}".format(name, year))

def fall_in_love(person1, person2):
    print("{} fell in love with {}".format(person1, person2))

def get_married(person1, person2):
    print("{} married {}".format(person1, person2))

if __name__ == "__main__":
    nick = 'Nick'
    melissa = 'Melissa'

    attend_CSU(nick, 2014)
    attend_CSU(melissa, 2014)
    fall_in_love(nick, melissa)

    NickAndMelissa = Process(target=get_married, args=(nick, melissa))
    NickAndMelissa.start()
    NickAndMelissa.join()

