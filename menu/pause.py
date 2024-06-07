from . import window
from . import menu
import pygame
from . import Draw_text
resume_rect = pygame.Rect(menu.x, 200, 175, 50)
settings_rect = pygame.Rect(menu.x, 280, 200, 50)
Quit_rect = pygame.Rect(menu.x, 360, 90, 50)
def draw_pause_screen():

    window.window.fill(window.green)
    Draw_text.draw_text('Resume', menu.font, menu.text_col, menu.x, 200)

    Draw_text.draw_text('Settings', menu.font, menu.text_col, menu.x, 280)

    Draw_text.draw_text('Quit', menu.font, menu.text_col, menu.x, 360)