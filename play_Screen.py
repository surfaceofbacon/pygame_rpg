import Draw_text
import window
import pygame
import menu

font = pygame.font.SysFont('Arialblack', 40)

back_rect = pygame.Rect(480, 380, 90, 50)
def Draw_Play_Screen():
    play_color = (0, 255, 255)
    text_color = (255, 0, 0)
    window.window.fill(play_color)
    Draw_text.draw_text('This is the play screen', font, text_color, 480, 280)
    Draw_text.draw_text('back', font, text_color, 480, 380)



