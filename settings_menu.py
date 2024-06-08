import Draw_text
import window
import pygame


font = pygame.font.SysFont('Arialblack', 40)
back_rect = pygame.Rect(480, 380, 90, 50)
blue_rect = pygame.Rect(400, 280, 90, 50)
red_rect = pygame.Rect(600, 280, 80, 50)
green_rect = pygame.Rect(800, 280, 130, 50)
def Draw_Settings_Menu():
    play_color = (100, 55, 25)
    text_color = (255, 70, 200)
    window.window.fill(play_color)
    Draw_text.draw_text('Settings Menu', font, text_color, 500, 100)
    Draw_text.draw_text('back', font, text_color, 500, 380)
    Draw_text.draw_text('Blue', font, window.blue, 400, 280)
    Draw_text.draw_text('Red', font, window.red, 600, 280)
    Draw_text.draw_text('Green', font, window.green, 800, 280)
