import pygame   #imports pygame to file

pygame.init()  #initilizes pygame so the window can run

size = 1280, 720   #defines the size of the window
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
gray = (128, 128, 128)


FPS = 60  #lock it to 60 fps
window = pygame.display.set_mode(size) #defines the window
clock = pygame.time.Clock()    #defines the clock


