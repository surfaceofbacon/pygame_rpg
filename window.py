import pygame   #imports pygame to file

pygame.init()  #initilizes pygame so the window can run

size = 1280, 720   #defines the size of the window


FPS = 60  #lock it to 60 fps
window = pygame.display.set_mode(size) #defines the window
clock = pygame.time.Clock()    #defines the clock


