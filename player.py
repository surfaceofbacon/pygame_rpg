import attack   # imports attack to the player can attack

class player:

    def __init__(self, armor, weapon,):    # innit method applies armor and a weapon to a player
        self.weapon = weapon
        self.armor = armor

    def attack(self, weapon, enemy):       # attack method gives the ability to attack enemies
        attack.attack(weapon, enemy)
