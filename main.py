import pygame

import actions
import attack
import boolean
import enemies
import window_refresh
import menu_nav
import player
import reset
import time

def main():    # the main function that draws the window and allows for functionality
    while boolean.running:
        window_refresh.refresh(player.hero)
        reset.reset()
        for event in pygame.event.get():
            menu_nav.menu_nav(event)
            if boolean.play:
                actions.check_actions(event, (player.cube_x, player.cube_y))

        






if __name__ == '__main__':     # runs the main function
    main()
