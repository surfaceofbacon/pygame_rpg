import Draw_text
import window
import pygame
import menu
import random
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)
background = pygame.image.load('testmap.png')
levels = [black, white, red, green, blue, yellow, cyan, magenta, gray]
random.shuffle(levels)

def Draw_Play_Screen(number):
    #window.window.blit(background, (0,0))
    window.window.fill(levels[number])



