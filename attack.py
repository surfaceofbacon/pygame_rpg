import random

def attack(weapon, enemy):
    range_cap = 100 // weapon.crit_chance
    hitDie = random.randint(1, 21)
    critCalc = random.randint(1, range_cap+1)

    if critCalc == 1:
        crit = True
        print('crit == True')
    else:
        crit = False
        print('crit == False')
    if hitDie + weapon.modifier > enemy.AC and critCalc == True:
        enemy.health -= (weapon.damage * 2)
        print('enemy has been hit')
    elif hitDie + weapon.modifier > enemy.AC:
        enemy.health -= weapon.damage
        print('enemy has been hit')
    else:
        print('you missed')
