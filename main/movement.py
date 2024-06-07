import pygame
import boolean
from player import player
from menu import play_Screen, window


def move_cube(x, y):

    keys = pygame.key.get_pressed()
    if x > window.size[0] - player.cube_width:
        player.cube_x = 0
        if play_Screen.number == 8:
            player.cube_x = window.size[0] - player.cube_width
        else:
            play_Screen.number += 1
    if x < 0:
        player.cube_x = window.size[0] - player.cube_width

        if play_Screen.number == 0:
            player.cube_x = 0
        else:
            play_Screen.number -= 1
    if y > window.size[1] - player.cube_height:
        player.cube_y = window.size[1] - player.cube_height
    if y < 0:
        player.cube_y = 0
    if keys[pygame.K_w]:
        player.cube_y -= player.speed
    if keys[pygame.K_s]:
        player.cube_y += player.speed
    if keys[pygame.K_a]:
        player.cube_x -= player.speed
    if keys[pygame.K_d]:
        player.cube_x += player.speed
    if keys[pygame.K_ESCAPE]:
        boolean.play = False
        boolean.bool_pause = True
