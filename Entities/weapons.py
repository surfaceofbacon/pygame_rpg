import pygame
from Entities import player
from Main import window, colors
import math
bullets = []
bullet_position = []
sword_range = 150
class Weapon:    # creates weapon class

    def __init__(self, name, modifier, damage, crit_chance, range):  # assigns modifier, damage, and crit_chance to
        # the instance of a weapon
        self.name = name
        self.modifier = modifier
        self.damage = damage
        self.crit_chance = crit_chance
        self.range = range

    def __str__(self):
        return self.name




class Bullet:

    def __init__(self, player_position: tuple):
        self.player_position = player_position
        self.speed = 10
        self.x_distance = (bullet_position[0][0] - self.player_position[0])
        self.y_distance = (bullet_position[0][1] - self.player_position[1])
        self.angle = math.atan(self.y_distance / self.x_distance)
        if self.x_distance > 0:
            self.angle += math.pi
        print(player_position)

    def draw(self):
        rectangle = (bullet_position[0][0], bullet_position[0][1], 10, 10)
        pygame.draw.rect(window.window, colors.black, rectangle)

    def move_bullet(self):
        bullet_position[0][0] += self.speed * math.cos(self.angle)
        bullet_position[0][1] += self.speed * math.sin(self.angle)


def spawn_bullet(enemy):
    bullet_position.append(enemy.position)
    bullet = Bullet((player.cube_x, player.cube_y))
    bullets.append(bullet)


stone_sword = Weapon('stone sword', 1, 3, 0, sword_range)
iron_sword = Weapon('iron sword', 3, 5, 3, sword_range)    # creates an instance of a weapon and assigns it to a iron sword

weapon_list = [stone_sword, iron_sword]
