import pygame
from . import settings_menu, start_menu, pause
from main import boolean


def menu_nav(events):
    if events.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if boolean.start_settings and settings_menu.back_rect.collidepoint(pos):
            boolean.start_settings = False
            boolean.start = True
        elif boolean.pause_settings and settings_menu.back_rect.collidepoint(pos):
            boolean.pause_settings = False
            boolean.bool_pause = True
        elif start_menu.play_rect.collidepoint(pos) and boolean.start:
            boolean.play = True
            boolean.start = False
        elif start_menu.settings_rect.collidepoint(pos) and boolean.start:
            boolean.start_settings = True
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
            boolean.pause_settings = True
    if events.type == pygame.QUIT:  # closes the window when the x is pressed
        boolean.running = False