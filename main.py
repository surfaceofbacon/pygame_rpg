import pygame

pygame.init()

size = 1280, 720

run = True

white = 255, 255, 255

window = pygame.display.set_mode(size)


def draw_window():
    window.fill(white)
    pygame.display.update()


def main():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()


if __name__ == '__main__':
    main()

