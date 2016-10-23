'''What is the probablity that in 24 rolls of a pair of dice one will roll 6 on both
the die'''

import random

def rollDie():
    return random.choice([1,2,3,4,5,6])



def game(trials, rolls):

    positive = 0.0
    for i in xrange(trials):
        for j in range(rolls):
            a = rollDie()
            b = rollDie()

            if a==6 and b==6:
                positive = positive + 1
                break

    return positive/trials

print game(10000000,24)

