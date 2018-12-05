__author__ = "Chris Gaudet"

class Warrior():
    """
    Describes a warrior
    """
    def __init__(self, name):
        """
        Initiates a warriors info
        :param name: Warriors name
        :param armor: warriors armor
        :param shield: warriors shield
        """
        self.name=name
        self.inventory= []

    def get_name(self):
        """
        A function to get the warriors name.
        :return: Warriors name
        """
        return self.name

    def set_inventory(self, weapon):
        """
        Sets the warriors inventory
        """
        self.inventory.append(weapon)


    def get_inventory(self):
        """
        A function to get the warriors inventory
        :return: warriors inventory
        """
        return self.inventory

    def set_dmg(self):
        dmg = 0
        for i in range(len(self.inventory)):
            dmg += self.inventory[i].get_dmg()
        self.dmg = dmg

    def set_defe(self):
        defe = 0
        for i in range(len(self.inventory)):
            defe += self.inventory[i].get_defe()
        self.defe = defe

    def get_dmg(self):
        """
        A function to get the warriors damage
        :return: warriors damage
        """
        return self.dmg

    def get_defe(self):
        """
        A function to get the warriors defence
        :return: Warriors defence
        """
        return self.defe


class Weapon():
    """
    weapons for the warrior
    """

    def __init__(self, name, dmg, defe):
        """
        Sets the information for a weapon
        :param name: Weapon name
        :param dmg: Weapon damage stats
        :param defe: weapon defence stats
        """
        self.name=name
        self.dmg=dmg
        self.defe = defe


    def get_name(self):
        """
        A function to get the weapon name
        :return: weapons name
        """
        return self.name

    def get_dmg(self):
        """
        A function to get the weapons damage
        :return: weapons damage
        """
        return self.dmg

    def get_defe(self):
        """
        A function to get the weapons defence
        :return: weapons defense
        """
        return self.defe

class Armory():
    """
    The armory for the warriors to pick their weapons from
    """
    def __init__(self):
        self.wepsnarmor = [
            Weapon("Bow&Arrow", 4, 1),
            Weapon("Katana", 3, 3),
            Weapon("No-Dachi", 2, 1),
            Weapon("Tanto", 4, 1),
            Weapon("Yoroi Armor", 0, 4),
            Weapon("The Dory", 3, 2),
            Weapon("Spartan Sword", 4, 2),
            Weapon("The Kopis", 4, 3),
            Weapon("Old Bashing Shield", 1, 4)
        ]
