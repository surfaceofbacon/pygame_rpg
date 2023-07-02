import pygame   #imports pygame to file



pygame.init()  #initilizes pygame so the window can run

size = 1280, 720   #defines the size of the window


white = 255, 255, 255  #the color of the window will be white
FPS = 60  #lock it to 60 fps
window = pygame.display.set_mode(size) #defines the window
clock = pygame.time.Clock()    #defines the clock

def draw_window():   #the function to draw the window
    window.fill(white)
    pygame.display.update()
