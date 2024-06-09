import time
import pygame
import main
import Draw_text
import start_menu
import settings_menu
import pause
import boolean
import player
import play_Screen
import window
import window_refresh


def menu_nav(events):
    time = pygame.time.get_ticks()
    if events.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if boolean.settings and settings_menu.back_rect.collidepoint(pos):
            boolean.settings = False
            boolean.start = True
        elif boolean.settings and settings_menu.back_rect.collidepoint(pos):
            boolean.settings = False
            boolean.bool_pause = True
        elif start_menu.play_rect.collidepoint(pos) and boolean.start:
            boolean.play = True
            boolean.start = False
        elif start_menu.settings_rect.collidepoint(pos) and boolean.start:
            boolean.settings = True
            boolean.start = False
        elif start_menu.Quit_rect.collidepoint(pos) and boolean.start:
            boolean.running = False
        elif pause.resume_rect.collidepoint(pos) and boolean.bool_pause:
            boolean.bool_pause = False
            boolean.play = True
        elif pause.Quit_rect.collidepoint(pos) and boolean.bool_pause:
            boolean.running = False
        elif pause.settings_rect.collidepoint(pos) and boolean.bool_pause:
            boolean.bool_pause = False
            boolean.settings = True
        if boolean.settings and settings_menu.blue_rect.collidepoint(pos):
            player.player_color = play_Screen.blue
            settings_menu.blue_color = window.black
        elif boolean.settings and settings_menu.red_rect.collidepoint(pos):
            player.player_color = play_Screen.red
            settings_menu.red_color = window.black
        elif boolean.settings and settings_menu.green_rect.collidepoint(pos):
            player.player_color = play_Screen.green
            settings_menu.green_color = window.black
    if events.type == pygame.QUIT:  # closes the window when the x is pressed
        boolean.running = False