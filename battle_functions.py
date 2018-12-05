__author__ = "Chris Gaudet"

import random
from NewClasses import *

def fight(warrior1, warrior2):
    """
    This function randomly chooses which warrior is attacking and calculates who wins
    :param warrior1: Spartan warrior
    :param warrior2: Samurai warrior
    :return: Either warrior1 or warrior2 depending on who was stronger
    """
    offensive = ("choice1", "choice2")
    attacker = random.choice(offensive)

    if attacker == "choice1":
        if warrior1.get_dmg() > warrior2.get_defe():
            return warrior1
        elif warrior1.get_dmg() < warrior2.get_defe():
            return warrior2
        else:
            return None
    if attacker == "choice2":
        if warrior2.get_dmg() > warrior1.get_defe():
            return warrior2
        elif warrior2.get_dmg() < warrior1.get_defe():
            return warrior1
        else:
            return None

def war(warrior1, warrior2):
    """
    Starts the battle between the two warriors
    :param warrior1: The spartan
    :param warrior2: The samurai
    """
    armory = Armory().wepsnarmor
    #Selects two random weapons from the armory and removes them so they cannot be picked again during that battle
    w1w1 = random.choice(armory)
    armory.remove(w1w1)
    w1w2 = random.choice(armory)
    armory.remove(w1w2)
    #Sets the selected weapons to warrior1
    warrior1.set_inventory(w1w1)
    warrior1.set_inventory(w1w2)

    # Selects two random weapons from the armory and removes them so they cannot be picked again during that battle
    w2w1 = random.choice(armory)
    armory.remove(w2w1)
    w2w2 = random.choice(armory)
    armory.remove(w2w2)
    #Sets the selected weapon to warrior2
    warrior2.set_inventory(w2w1)
    warrior2.set_inventory(w2w2)

    #Set the damage and defence for the first warrior
    warrior1.set_dmg()
    warrior1.set_defe()

    #Set the damage and defence for the second warrior
    warrior2.set_dmg()
    warrior2.set_defe()

    SpartanWins = 0
    SamuraiWins = 0
    for x in range(0,10):
        winner = fight(warrior1, warrior2)
        if winner == warrior1:
            SpartanWins += 1
        if winner == warrior2:
            SamuraiWins += 1
        if winner == None:
            pass

    if SpartanWins > SamuraiWins:
        return warrior1
    elif SpartanWins < SamuraiWins:
        return warrior2
    else:
        return None