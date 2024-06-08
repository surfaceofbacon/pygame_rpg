import attack   # imports the attack module to apply that to enemies


class Enemy:   # class of an enemy

    def __init__(self, AC, health):     # innit method gives the instance of an enemy armor class and health
        self.AC = AC
        self.health = health


    def attack(self, weapon):           # attack method gives enemies the ability to attack
        attack.attack(weapon, enemy=player)


skeleton = Enemy(15, 10)  # creates an instance of an enemy and assigns it to a skeleton
