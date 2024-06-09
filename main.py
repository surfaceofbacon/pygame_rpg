import pygame
import boolean
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

        






if __name__ == '__main__':     # runs the main function
    main()
