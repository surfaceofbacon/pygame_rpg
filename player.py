import attack

class player:

    def __init__(self, armor, weapon,):
        self.weapon = weapon
        self.armor = armor

    def attack(self, weapon, enemy):
        attack.attack(weapon, enemy)
