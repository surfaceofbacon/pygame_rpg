from Main import window, colors
import pygame
from Entities import player
from Menu import Draw_text

font = pygame.font.SysFont('Arialblack', 40)
resume_rect = pygame.Rect(500, 200, 175, 50)
settings_rect = pygame.Rect(500, 280, 200, 50)
Quit_rect = pygame.Rect(500, 360, 90, 50)
def draw_pause_screen():

    window.window.fill(colors.green)
    Draw_text.draw_text('Resume', font, colors.black, 500, 200)

    Draw_text.draw_text('Settings', font, colors.black, 500, 280)

    Draw_text.draw_text('Quit', font, colors.black, 500, 360)

    Draw_text.draw_text(f'{player.hero.weapon}', font, colors.black, 250, 280)
