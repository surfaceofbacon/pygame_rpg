import enemies

def check(enemy):
    if enemy.tick_speed <= 0:
        enemy.attack()
        enemy.tick_speed = enemies.triangle_tick_speed
    else:
        enemy.tick_speed -= 1


