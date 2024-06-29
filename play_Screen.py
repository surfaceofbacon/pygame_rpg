import boolean
import enemies
import window
import random
import colors
levels = [colors.black, colors.white, colors.red, colors.green, colors.blue, colors.yellow, colors.cyan, colors.magenta, colors.gray]
number = 0
random.shuffle(levels)

def Draw_Play_Screen(number):
    window.window.fill(levels[number])
    if not boolean.generated:
        enemies.enemies_list.clear()
        generate_level(number)

def generate_level(number):
    if levels[number] == colors.black:
        triangle_enemy1 = enemies.Triangle(10, 10, 1, [100, 100])
        triangle_enemy2 = enemies.Triangle(10, 10, 1, [500, 500])
        enemies.enemies_list.append(triangle_enemy1)
        enemies.enemies_list.append(triangle_enemy2)
    boolean.generated = True



