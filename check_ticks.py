import enemies


def check(enemy):
    if enemy.tick <= 0:
        enemy.attack()
        enemy.tick = enemy.tick_speed
    else:
        enemy.tick -= 1


