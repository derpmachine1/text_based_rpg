from entity import Entity
from random import randint


# Class for player
class Player(Entity):
    def __init__(self, name, difficulty):
        super().__init__(name)

        self.difficulty = difficulty

        # Variables to store base stats
        self.hp_max_base = int(round(100 / self.difficulty))
        self.mp_max_base = int(round(100 / self.difficulty))
        self.hp_base = self.hp_max_base
        self.mp_base = self.mp_max_base
        self.attack_base = int(round(10 / self.difficulty))
        self.defense_base = 0

        # Variables to store final stats; will be used in the future for equipment, status effects, etc
        self.hp_max = self.hp_max_base
        self.mp_max = self.mp_max_base
        self.hp = self.hp_base
        self.mp = self.mp_base
        self.attack = self.attack_base
        self.defense = self.defense_base

        self.exp = 0
        self.exp_req = 0
        self.lvl = 1

    # Adds modifiers to base stats
    def calculate_final_stats(self):
        self.hp_max = self.hp_max_base
        self.mp_max = self.mp_max_base
        self.hp = self.hp_base
        self.mp = self.mp_base
        self.attack = self.attack_base
        self.defense = self.defense_base

    # Calculates exp required to next level and handles level ups
    def calculate_lvl(self):
        self.exp_req = self.lvl * 10

        if self.exp >= self.exp_req:
            self.lvl += 1
            self.exp -= self.exp_req

            # Increases base stats
            x = randint(5, 15)
            self.hp_max_base += x
            self.hp_base += x
            x = randint(5, 15)
            self.mp_max_base += x
            self.mp_base += x
            self.attack_base += randint(1, 3)

            self.exp_req = self.lvl * 10

    # Updates everything about the player
    def update(self):
        self.calculate_final_stats()
        self.calculate_lvl()

    # Displays player stats
    def display(self):
        print("| {:32} | {:8}{:>24} |".format(self.name, "LVL " + str(self.lvl) + ":", str(self.exp) + "/" + str(self.exp_req)))
        print("| {:8}{:>24} | {:8}{:>24} |".format("HP:", str(self.hp) + "/" + str(self.hp_max), "MP:", str(self.mp) + "/" + str(self.mp_max)))
        print("| {:8}{:>24} | {:8}{:>24} |".format("ATT:", str(self.attack), "DEF:", str(self.defense)))

    def change_hp(self, d_hp):
        self.hp_base += d_hp
        self.hp += d_hp

    def change_mp(self, d_mp):
        self.mp_base = d_mp
        self.mp += d_mp
