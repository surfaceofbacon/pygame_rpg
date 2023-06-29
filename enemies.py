import attack


class Enemy:

    def __init__(self, AC, health):
        self.AC = AC
        self.health = health


    def attack(self, weapon):
        attack.attack(weapon, enemy = player)


skeleton = Enemy(15, 10)
