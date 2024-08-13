import boolean
import weapons
import enemies
import window
import player
import colors
levels = [colors.black, colors.white, colors.red, colors.green, colors.blue, colors.yellow, colors.cyan, colors.magenta, colors.gray]
number = 0
#random.shuffle(levels)


def Draw_Play_Screen(num):
    window.window.fill(levels[num])
    if not boolean.generated:
        enemies.enemies_list.clear()
        generate_level(num)


def generate_level(num):
    if levels[num] == colors.black:
        triangle_enemy1 = enemies.Triangle([100, 100])
        triangle_enemy2 = enemies.Triangle([500, 500])
        enemies.enemies_list.append(triangle_enemy1)
        enemies.enemies_list.append(triangle_enemy2)

    elif levels[num] == colors.white:
        pentagon_enemy = enemies.Pentagon([100, 100])
        enemies.enemies_list.append(pentagon_enemy)

    boolean.generated = True


