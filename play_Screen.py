import Draw_text
import window
import pygame


font = pygame.font.SysFont('Arialblack', 40)


def Draw_Play_Screen():
    play_color = (0, 255, 255)
    text_color = (255, 0, 0)
    window.window.fill(play_color)
    Draw_text.draw_text('This is the play screen', font, text_color, 480, 280)




