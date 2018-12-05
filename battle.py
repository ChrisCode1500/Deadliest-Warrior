__author__ = "Chris Gaudet"

from battle_functions import *

w1wins = 0
w2wins = 0
for i in range(0,500):
    warrior1 = Warrior("Spartan")
    warrior2 = Warrior("Samurai")

    simulation = war(warrior1, warrior2)
    if simulation == warrior1:
        w1wins += 1
    elif simulation == warrior2:
        w2wins += 1
print("Spartan wins: ", w1wins)
print("Samurai wins: ", w2wins)

