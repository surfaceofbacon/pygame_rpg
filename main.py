import window, pygame, play_Screen, start_menu, settings_menu, player, pause, movement, boolean


def main():    # the main function that draws the window and allows for functionality
    hero = player.player(10, player.cube_width, player.cube_height)
    while boolean.running:
        if boolean.start:
            start_menu.start_menu()
        pygame.display.update()
        window.clock.tick(window.FPS)
        if boolean.play:
            play_Screen.Draw_Play_Screen(play_Screen.number)
            movement.move_cube(player.cube_x, player.cube_y)
            hero.cube(player.cube_x, player.cube_y)
        if boolean.start_settings:
            settings_menu.Draw_Settings_Menu()
        if boolean.pause_settings:
            settings_menu.Draw_Settings_Menu()
        if boolean.bool_pause:
            pause.draw_pause_screen()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boolean.start_settings and settings_menu.back_rect.collidepoint(pos):
                    boolean.start_settings = False
                    boolean.start = True
                if boolean.pause_settings and settings_menu.back_rect.collidepoint(pos):
                    boolean.pause_settings = False
                    boolean.bool_pause = True
                if start_menu.play_rect.collidepoint(pos) and boolean.start:
                    boolean.play = True
                    boolean.start = False
                elif start_menu.settings_rect.collidepoint(pos) and boolean.start:
                    boolean.start_settings = True
                    boolean.start = False
                elif start_menu.Quit_rect.collidepoint(pos) and boolean.start:
                    boolean.running = False
                if pause.resume_rect.collidepoint(pos) and boolean.bool_pause:
                    boolean.bool_pause = False
                    boolean.play = True
                elif pause.Quit_rect.collidepoint(pos) and boolean.bool_pause:
                    boolean.running = False
                elif pause.settings_rect.collidepoint(pos) and boolean.bool_pause:
                    boolean.bool_pause = False
                    boolean.pause_settings = True

            if event.type == pygame.QUIT:  # closes the window when the x is pressed
                boolean.running = False

        






if __name__ == '__main__':     # runs the main function
    main()
