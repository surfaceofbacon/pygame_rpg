import pygame
from Actions import actions
from Menu import menu_nav
from Entities import player
from Main import reset, window_refresh, boolean


def main():    # the main function that draws the window and allows for functionality
    while boolean.running:
        window_refresh.refresh(player.hero)
        reset.reset()
        for event in pygame.event.get():
            menu_nav.menu_nav(event)
            if boolean.play:
                actions.check_actions_hero(event, (player.cube_x, player.cube_y))
        actions.check_actions_enemies((player.cube_x, player.cube_y))



        






if __name__ == '__main__':     # runs the main function
    main()
