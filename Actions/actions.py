import pygame
import math
from Actions import attack, check_ticks
from Entities import enemies, weapons

def check_actions_hero(event, player_position: tuple):
    for enemy in enemies.enemies_list:
        distance = math.sqrt((player_position[0]-enemy.position[0])**2 + (player_position[1]-enemy.position[1])**2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and distance < weapons.iron_sword.range:
                attack.attack(weapons.iron_sword, enemy)
def check_actions_enemies(player_position):
    for enemy in enemies.enemies_list:
        distance = math.sqrt((player_position[0] - enemy.position[0]) ** 2 + (player_position[1] - enemy.position[1]) ** 2)
        if distance <= enemy.range:
            check_ticks.check(enemy)


