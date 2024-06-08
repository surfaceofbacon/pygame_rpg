import pygame

import play_Screen

import play_Screen
import window
import Draw_text
font = pygame.font.SysFont('Arialblack', 40)
play_rect = pygame.Rect(500, 200, 90, 50)
settings_rect = pygame.Rect(500, 280, 200, 50)
Quit_rect = pygame.Rect(500, 360, 90, 50)


def start_menu():
    window.window.fill(play_Screen.green)

    Draw_text.draw_text('Play', font, play_Screen.black, 500, 200)

    Draw_text.draw_text('Settings', font, play_Screen.black, 500, 280)

    Draw_text.draw_text('Quit', font, play_Screen.black, 500, 360)
