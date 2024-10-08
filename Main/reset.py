from Entities import enemies, player
from Main import boolean, colors
from Menu import play_Screen, settings_menu
import random


def reset():
    settings_menu.blue_color = colors.blue
    settings_menu.red_color = colors.red
    settings_menu.green_color = colors.green

def game_reset():
    boolean.play = False
    boolean.bool_pause = False
    boolean.start = True
    boolean.settings = False
    boolean.running = True
    boolean.generated = False
    boolean.dead = False
    enemies.enemies_list = []
    play_Screen.number = 0
    random.shuffle(play_Screen.levels)
    player.speed = 15
    player.cube_x = 700
    player.cube_y = 400
    player.cube_width = 100
    player.cube_height = 100
    player.hero.health = 10

