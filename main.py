import window, pygame, play_loop, play_Screen, start_menu, settings_menu


def main():    # the main function that draws the window and allows for functionality
    start = True
    play = False
    settings = False
    running = True
    while running:

        if start:
            start_menu.start_menu()

        pygame.display.update()

        window.clock.tick(window.FPS)
        if play:
            play_Screen.Draw_Play_Screen()
        if settings:
            settings_menu.Draw_Settings_Menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play and play_Screen.back_rect.collidepoint(pos):
                    play = False
                    start = True
                if settings and settings_menu.back_rect.collidepoint(pos):
                    settings = False
                    start = True
                if start_menu.play_rect.collidepoint(pos) and start:
                    play = True
                    start = False
                elif start_menu.settings_rect.collidepoint(pos) and start:
                    settings = True
                    start = False
                elif start_menu.Quit_rect.collidepoint(pos) and start:
                    running = False
            if event.type == pygame.QUIT:  # closes the window when the x is pressed
                running = False


if __name__ == '__main__':     # runs the main function
    main()
