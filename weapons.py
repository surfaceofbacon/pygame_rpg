class Weapon:    # creates weapon class

    def __init__(self, modifier, damage, crit_chance, range):  # assigns modifier, damage, and crit_chance to
        # the instance of a weapon
        self.modifier = modifier
        self.damage = damage
        self.crit_chance = crit_chance
        self.range = range


iron_sword = Weapon(3, 5, 3, 150)    # creates an instance of a weapon and assigns it to a iron sword

