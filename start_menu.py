import pygame
import colors
import window
import Draw_text
font = pygame.font.SysFont('Arialblack', 40)
play_rect = pygame.Rect(500, 200, 90, 50)
settings_rect = pygame.Rect(500, 280, 200, 50)
Quit_rect = pygame.Rect(500, 360, 90, 50)


def start_menu():
    window.window.fill(colors.green)

    Draw_text.draw_text('Play', font, colors.black, 500, 200)

    Draw_text.draw_text('Settings', font, colors.black, 500, 280)

    Draw_text.draw_text('Quit', font, colors.black, 500, 360)
