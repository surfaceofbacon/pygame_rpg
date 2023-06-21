import pygame



pygame.init()

size = 1280, 720

run = True

white = 255, 255, 255
FPS = 60
window = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def draw_window():
    window.fill(white)
    pygame.display.update()
