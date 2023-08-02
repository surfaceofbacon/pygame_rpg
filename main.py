import window
import pygame
import weapons
import enemies
import attack
import menu
import Draw_text


def main():    # the main function that draws the window and allows for functionality

    running = True
    while running:
        window.window.fill(menu.color)

        Draw_text.draw_text('Play', menu.font, menu.text_col, menu.x, 200)
        Draw_text.draw_text('Settings', menu.font, menu.text_col, menu.x, 280)
        Draw_text.draw_text('Quit', menu.font, menu.text_col, menu.x, 360)

        pygame.display.update()

        window.clock.tick(window.FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key =
            if event.type == pygame.QUIT:  # closes the window when the x is pressed
                running = False


    attack.attack(weapon=weapons.iron_sword, enemy=enemies.skeleton)
    print(enemies.skeleton.health)


if __name__ == '__main__':  # runs the main function
    main()
