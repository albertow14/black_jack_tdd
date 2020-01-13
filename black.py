import random

desk = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,10,10,10,10,10,10,10,10]

def givecard(desk):
    return random.choice(desk)

def eliminate(num, desk)