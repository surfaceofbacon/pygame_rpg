import random    # imports the random module as this funcion requires a lot of random integers


def attack(weapon, enemy):        # defines the function for attacking
    range_cap = 100 // weapon.crit_chance    # so we can calculate the chance of getting a crit hit with critCalc
    hitDie = random.randint(1, 21)       # hits are random chance with d20s
    critCalc = random.randint(1, range_cap+1)    # calculates if there is a crit hit or not

    if critCalc == 1:   # if critCalc is one then it's a crit
        crit = True
        print('crit == True')
    else:                                # any other number and it is not a crit
        crit = False
        print('crit == False')
    if hitDie + weapon.modifier > enemy.AC and crit:  # assigns damage to enemy with critical damage
        enemy.health -= (weapon.damage * 2)
        print('enemy has been hit')
    elif hitDie + weapon.modifier > enemy.AC:     # assigns damage to enemy
        enemy.health -= weapon.damage
        print('enemy has been hit')
    else:   # misses the shot
        print('you missed')
