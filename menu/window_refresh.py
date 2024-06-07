import pygame, movement
from player import player
from menu import pause, play_Screen, start_menu, settings_menu, window
from main import boolean


def refresh(hero):
    if boolean.start:
        start_menu.start_menu()
    pygame.display.update()
    window.clock.tick(window.FPS)
    keys = pygame.key.get_pressed()
    if boolean.play:
        play_Screen.Draw_Play_Screen(play_Screen.number)
        movement.move_cube(player.cube_x, player.cube_y, keys)
        hero.cube(player.cube_x, player.cube_y)
    if boolean.start_settings:
        settings_menu.Draw_Settings_Menu()
    if boolean.pause_settings:
        settings_menu.Draw_Settings_Menu()
    if boolean.bool_pause:
        pause.draw_pause_screen()
