import pygame
import boolean
from menu import menu_nav, window_refresh
from player import player

def main():    # the main function that draws the window and allows for functionality
    hero = player.player(10, player.cube_width, player.cube_height)
    while boolean.running:
        window_refresh.refresh(hero)
        for event in pygame.event.get():
            menu_nav.menu_nav(event)

        






if __name__ == '__main__':     # runs the main function
    main()
