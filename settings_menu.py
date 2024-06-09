import Draw_text
import window
import pygame


font = pygame.font.SysFont('Arialblack', 40)
back_rect = pygame.Rect(480, 380, 90, 50)
blue_rect = pygame.Rect(400, 280, 90, 50)
red_rect = pygame.Rect(600, 280, 80, 50)
green_rect = pygame.Rect(800, 280, 130, 50)
blue_color = window.blue
red_color = window.red
green_color = window.green
settings_color = (255, 70, 200)
back_color = (255, 70, 200)
def Draw_Settings_Menu():
    play_color = (100, 55, 25)
    window.window.fill(play_color)
    Draw_text.draw_text('Settings Menu', font, settings_color, 500, 100)
    Draw_text.draw_text('back', font, back_color, 500, 380)
    Draw_text.draw_text('Blue', font, blue_color, 400, 280)
    Draw_text.draw_text('Red', font, red_color, 600, 280)
    Draw_text.draw_text('Green', font, green_color, 800, 280)
