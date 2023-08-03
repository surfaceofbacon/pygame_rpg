import pygame

import window
import Draw_text
import menu

play_rect = pygame.Rect(menu.x, 200, 90, 50)
settings_rect = pygame.Rect(menu.x, 280, 90, 50)
Quit_rect = pygame.Rect(menu.x, 360, 90, 50)
def start_menu():
    window.window.fill(menu.color)


    Draw_text.draw_text('Play', menu.font, menu.text_col, menu.x, 200)

    Draw_text.draw_text('Settings', menu.font, menu.text_col, menu.x, 280)

    Draw_text.draw_text('Quit', menu.font, menu.text_col, menu.x, 360)
