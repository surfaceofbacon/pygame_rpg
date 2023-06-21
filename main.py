import window
import pygame
import weapons
import enemies
import attack





def main():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.draw_window()
        window.clock.tick(window.FPS)
    attack.attack(weapon=weapons.iron_sword, enemy=enemies.skeleton)
    print(enemies.skeleton.health)


if __name__ == '__main__':
    main()
