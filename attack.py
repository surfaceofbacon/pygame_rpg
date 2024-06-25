import dice


def attack(weapon, enemy):        # defines the function for attacking
    range_cap = 100 // weapon.crit_chance    # so we can calculate the chance of getting a crit hit with critCalc
    hitDie = dice.roll_dice(20, weapon.modifier)      # hits are random chance with d20s
    critCalc = dice.roll_dice(range_cap, 0)    # calculates if there is a crit hit or not

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
    if enemy.health <= 0:
        enemy.kill()

