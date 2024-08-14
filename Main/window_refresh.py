import pygame
from Main import reset, boolean
from Main import window
from Menu import pause, play_Screen, settings_menu, start_menu
from Entities import enemies, player, weapons, movement


def refresh(hero):
    if boolean.start:
        start_menu.start_menu()
    pygame.display.update()
    window.clock.tick(window.FPS)
    keys = pygame.key.get_pressed()
    if boolean.play:
        player_position = (player.cube_x, player.cube_y)
        play_Screen.Draw_Play_Screen(play_Screen.number)
        movement.move_cube(player.cube_x, player.cube_y, keys)
        hero.cube(player.cube_x, player.cube_y)
        hero.check_color()
        for enemy in enemies.enemies_list:
            enemy.draw(10)
            enemy.check_color()
            enemy.move_enemy(player_position, enemy.position)
        for bullet in weapons.bullets:

            bullet.draw()
            bullet.move_bullet()
        if hero.health <= 0:
            reset.game_reset()
    if boolean.settings:
        settings_menu.Draw_Settings_Menu()
    if boolean.bool_pause:
        pause.draw_pause_screen()
