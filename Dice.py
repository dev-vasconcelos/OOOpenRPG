from random import randint

#class Dice:

#    def __init__(self):
#        pass

def dmgLucky(atck, lucky, dex):
    return randint(0, atck) * randint(1, lucky) * dex // 8

def heal(heal):
    return randint(heal // 2, heal * 1.5)
