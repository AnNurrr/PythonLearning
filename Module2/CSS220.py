import random

# Ainur Emilbekova
#1/23/24

# Tails and Heads probability


#function to create a random number that is either heads or tails
def coinFlip():
    heads =0

    for i in range(100):
        if random.random() <= 0.5: # determines if it is heads
            heads +=1
    return heads

def simulate(n):
    trials =[]
    for i in range(n):
        trials.append(coinFlip())
    return sum(trials)/n

simulate(1)
simulate(10)
simulate(100)

