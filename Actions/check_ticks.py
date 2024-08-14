from Entities import enemies, weapons


def check(enemy):
    if enemy.tick <= 0 and type(enemy) == enemies.Hexagon:
        print('shoot')
        weapons.spawn_bullet(enemy)
        enemy.tick = enemy.tick_speed
    elif enemy.tick <= 0:
        enemy.attack()
        enemy.tick = enemy.tick_speed
    else:
        enemy.tick -= 1


