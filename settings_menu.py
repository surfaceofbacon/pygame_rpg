import Draw_text
import window
import pygame


font = pygame.font.SysFont('Arialblack', 40)


def Draw_Settings_Menu():
    play_color = (100, 55, 25)
    text_color = (255, 70, 200)
    window.window.fill(play_color)
    Draw_text.draw_text('This is the settings menu', font, text_color, 480, 280)
