import window
import random
import colors
import pygame
import draw_shape
#background = pygame.image.load('../testmap.png')
levels = [colors.black, colors.white, colors.red, colors.green, colors.blue, colors.yellow, colors.cyan, colors.magenta, colors.gray]
number = 0
random.shuffle(levels)

def Draw_Play_Screen(number):
    #window.window.blit(background, (0,0))
    window.window.fill(levels[number])



