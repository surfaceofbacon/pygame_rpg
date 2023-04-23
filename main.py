import pygame
import random
import weapons
import enemies
import armor

pygame.init()

size = 1280, 720

run = True

white = 255, 255, 255

window = pygame.display.set_mode(size)


def draw_window():
    window.fill(white)
    pygame.display.update()


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


def main():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()
    attack(weapon=weapons.iron_sword, enemy=enemies.skeleton)
    print(enemies.skeleton.health)


if __name__ == '__main__':
    main()
