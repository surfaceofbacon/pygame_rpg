import window
import pygame
import Draw_text
import play_Screen
font = pygame.font.SysFont('Arialblack', 40)
resume_rect = pygame.Rect(500, 200, 175, 50)
settings_rect = pygame.Rect(500, 280, 200, 50)
Quit_rect = pygame.Rect(500, 360, 90, 50)
def draw_pause_screen():

    window.window.fill(window.green)
    Draw_text.draw_text('Resume', font, window.black, 500, 200)

    Draw_text.draw_text('Settings', font, window.black, 500, 280)

    Draw_text.draw_text('Quit',font , play_Screen.black, 500, 360)
