import window
import pygame
import weapons
import enemies
import attack





def main():    # the main function that draws the window and allows for functionality

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closes the window when the x is pressed
                running = False
        window.draw_window()   # draws the window
        window.clock.tick(window.FPS)  # refreshes 6o times per second
    attack.attack(weapon=weapons.iron_sword, enemy=enemies.skeleton)
    print(enemies.skeleton.health)


if __name__ == '__main__':  # runs the main function
    main()
