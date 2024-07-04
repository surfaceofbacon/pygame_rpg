import pygame
import actions
import movement
import player
import reset
import window
import start_menu
import settings_menu
import play_Screen
import pause
import boolean
import enemies

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
            movement.move(player_position, enemy)
        if hero.health <= 0:
            reset.game_reset()
    if boolean.settings:
        settings_menu.Draw_Settings_Menu()
    if boolean.bool_pause:
        pause.draw_pause_screen()
